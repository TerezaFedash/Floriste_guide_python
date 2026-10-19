from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.db.models import Q, Avg, Count, Min, Max
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from catalog.models import Category, Occasion, Flower, CareGuide, Favorite
from catalog.forms import (
    FlowerForm,
    CareGuideForm,
    FlowerFilterForm,
    FloristConsultationForm,
    UserRegistrationForm,
)


# ==============================================================================
# 1. FUNCTION-BASED VIEWS (В6.2, Д4)
# ==============================================================================

def home_view(request):
    """
    В6.2 (FBV): Головна сторінка довідника флориста.
    Д4: Розрахунок зведеної аналітики та агрегованих показників за допомогою
    aggregate() та annotate().
    Д5: Оптимізація запитів за допомогою select_related.
    """
    # Агрегація загальної статистики каталогу (Д4)
    stats = Flower.objects.aggregate(
        total_flowers=Count("id"),
        avg_price=Avg("price"),
        min_price=Min("price"),
        max_price=Max("price"),
    )

    # Анотація: кількість квітів у кожній категорії (Д4)
    categories_with_counts = Category.objects.annotate(
        flower_count=Count("flowers")
    ).filter(flower_count__gt=0)

    # Добірка рекомендованих свіжих квітів (Д5: без N+1)
    featured_flowers = Flower.objects.filter(in_stock=True).select_related(
        "category", "owner"
    ).prefetch_related("occasions")[:4]

    # Список приводів для швидкого підбору
    occasions = Occasion.objects.all()[:6]

    context = {
        "stats": stats,
        "categories_with_counts": categories_with_counts,
        "featured_flowers": featured_flowers,
        "occasions": occasions,
    }
    return render(request, "catalog/home.html", context)


def consultation_view(request):
    """
    В5.2, В6.2 (FBV): Форма замовлення консультації флориста.
    Використовує forms.Form, не прив'язану до моделі.
    Реалізує шаблон Post/Redirect/Get (PRG) (В5.4).
    """
    if request.method == "POST":
        form = FloristConsultationForm(request.POST)
        if form.is_valid():
            client_name = form.cleaned_data["client_name"]
            occasion = form.cleaned_data["occasion_description"]
            # У навчальному проєкті запит успішно обробляється та відправляється флористу
            messages.success(
                request,
                f"Дякуємо, {client_name}! Ваш запит на підбір букета до події «{occasion}» "
                f"успішно надіслано черговому флористу. Ми зв'яжемося з Вами найближчим часом!"
            )
            return redirect("catalog:consultation")
    else:
        form = FloristConsultationForm()

    return render(request, "catalog/consultation.html", {"form": form})


@login_required
@require_POST
def toggle_favorite_view(request, pk):
    """
    В6.2, В5.4 (FBV): Додавання / вилучення квітки з обраного.
    Зміна даних виключно через POST з PRG.
    """
    flower = get_object_or_404(Flower, pk=pk)
    fav_obj = Favorite.objects.filter(user=request.user, flower=flower).first()

    if fav_obj:
        fav_obj.delete()
        messages.info(request, f"Квітку «{flower.name}» видалено з Вашого обраного.")
    else:
        Favorite.objects.create(user=request.user, flower=flower)
        messages.success(request, f"Квітку «{flower.name}» успішно додано до обраного! 🌸")

    # Повернення на сторінку, звідки надійшов запит, або до списку
    next_url = request.POST.get("next")
    if next_url and next_url.startswith("/"):
        return redirect(next_url)
    return redirect("catalog:flower_detail", pk=flower.pk)


# ==============================================================================
# 2. CRUD GENERIC VIEWS ДЛЯ ОСНОВНОЇ СУТНОСТІ FLOWER (В6.1, В6.3, В6.4)
# ==============================================================================

class FlowerListView(ListView):
    """
    В6.1 (ListView): Каталог квітів.
    В6.3: Пагінація списку (paginate_by = 6).
    В6.4: Перевизначення get_queryset() та get_context_data().
    Д4: Пошук та фільтрація через Q-об'єкти.
    Д5: Оптимізація select_related та prefetch_related без N+1 запитів.
    """
    model = Flower
    template_name = "catalog/flower_list.html"
    context_object_name = "flowers"
    paginate_by = 6

    def get_queryset(self):
        # Д5: Усунення проблеми N+1 запитів
        qs = Flower.objects.select_related("category", "owner").prefetch_related("occasions")

        # Читання фільтрів з GET-параметрів
        self.filter_form = FlowerFilterForm(self.request.GET)
        if self.filter_form.is_valid():
            q = self.filter_form.cleaned_data.get("q")
            category = self.filter_form.cleaned_data.get("category")
            occasion = self.filter_form.cleaned_data.get("occasion")
            max_price = self.filter_form.cleaned_data.get("max_price")
            in_stock_only = self.filter_form.cleaned_data.get("in_stock_only")

            # Д4: Пошук за допомогою Q-об'єктів (В8.1 - безпечна параметризація)
            if q:
                qs = qs.filter(
                    Q(name__icontains=q)
                    | Q(latin_name__icontains=q)
                    | Q(description__icontains=q)
                )
            if category:
                qs = qs.filter(category=category)
            if occasion:
                qs = qs.filter(occasions=occasion)
            if max_price is not None:
                qs = qs.filter(price__lte=max_price)
            if in_stock_only:
                qs = qs.filter(in_stock=True)

        return qs.distinct()

    def get_context_data(self, **kwargs):
        # В6.4: Перевизначення get_context_data()
        context = super().get_context_data(**kwargs)
        context["filter_form"] = self.filter_form
        context["total_found"] = self.get_queryset().count()
        return context


class FlowerDetailView(DetailView):
    """
    В6.1 (DetailView): Детальна сторінка квітки.
    В6.5: Маршрут із конвертером <int:pk>.
    Д5: Оптимізація доступу до зв'язаного довідника догляду (care_guide).
    """
    model = Flower
    template_name = "catalog/flower_detail.html"
    context_object_name = "flower"

    def get_queryset(self):
        return Flower.objects.select_related(
            "category", "owner", "care_guide"
        ).prefetch_related("occasions")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        flower = self.object
        user = self.request.user
        context["is_favorited"] = (
            user.is_authenticated
            and Favorite.objects.filter(user=user, flower=flower).exists()
        )
        # Схожі квіти з тієї ж категорії
        context["related_flowers"] = Flower.objects.filter(
            category=flower.category
        ).exclude(pk=flower.pk)[:3]
        return context


class FlowerCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """
    В6.1 (CreateView): Створення нової квітки.
    Доступ дозволено виключно адміністратору системи (is_superuser).
    В7.2: Власник запису присвоюється у form_valid(), а не вибирається у формі.
    """
    model = Flower
    form_class = FlowerForm
    template_name = "catalog/flower_form.html"

    def test_func(self):
        user = self.request.user
        return user.is_authenticated and user.is_superuser

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return super().handle_no_permission()
        messages.error(
            self.request,
            "Лише адміністратор має право додавати нові квіти до каталогу. Флористи та клієнти не мають доступу до цієї дії."
        )
        return redirect("catalog:flower_list")

    def form_valid(self, form):
        # В7.2: Присвоєння автора на рівні сервера
        form.instance.owner = self.request.user
        messages.success(self.request, f"Квітку «{form.instance.name}» успішно додано до каталогу адміністратором!")
        return super().form_valid(form)


class OwnerOrStaffRequiredMixin(UserPassesTestMixin):
    """
    В7.3, В7.5: Заборона редагування та видалення чужих записів.
    Перевірка прав доступу на сервері: редагувати запис може лише його автор або персонал (staff/флорист).
    """
    def test_func(self):
        obj = self.get_object()
        user = self.request.user
        return user.is_authenticated and (
            obj.owner == user or user.is_staff or user.groups.filter(name="Флористи").exists()
        )

    def handle_no_permission(self):
        messages.error(self.request, "У Вас недостатньо прав для зміни чи видалення цього запису.")
        return redirect("catalog:flower_list")


class FlowerUpdateView(LoginRequiredMixin, OwnerOrStaffRequiredMixin, UpdateView):
    """
    В6.1 (UpdateView): Редагування існуючої квітки.
    В7.3: Тільки автор запису або привілейована роль флориста.
    """
    model = Flower
    form_class = FlowerForm
    template_name = "catalog/flower_form.html"

    def form_valid(self, form):
        messages.success(self.request, f"Дані квітки «{form.instance.name}» успішно оновлено!")
        return super().form_valid(form)


class FlowerDeleteView(LoginRequiredMixin, OwnerOrStaffRequiredMixin, DeleteView):
    """
    В6.1 (DeleteView): Видалення квітки з підтвердженням.
    В5.4: Видалення через POST з PRG.
    """
    model = Flower
    template_name = "catalog/flower_confirm_delete.html"
    success_url = reverse_lazy("catalog:flower_list")

    def form_valid(self, form):
        flower_name = self.object.name
        response = super().form_valid(form)
        messages.warning(self.request, f"Квітку «{flower_name}» було успішно видалено з бази даних.")
        return response


# ==============================================================================
# 3. GENERIC VIEWS ДЛЯ ІНШИХ МОДЕЛЕЙ (В6.1)
# ==============================================================================

class CareGuideListView(ListView):
    """
    В6.1 (ListView для другої моделі): Каталог довідників з догляду.
    """
    model = CareGuide
    template_name = "catalog/careguide_list.html"
    context_object_name = "guides"
    paginate_by = 6

    def get_queryset(self):
        return CareGuide.objects.select_related("flower", "expert").order_by("flower__name")


class CareGuideDetailView(DetailView):
    """
    В6.1 (DetailView для другої моделі): Детальні інструкції з догляду.
    """
    model = CareGuide
    template_name = "catalog/careguide_detail.html"
    context_object_name = "guide"

    def get_queryset(self):
        return CareGuide.objects.select_related("flower", "expert")


class CareGuideCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """
    В7.4, В7.5: Привілейована дія — створення довідника догляду.
    Дозволено лише користувачам із правом 'can_manage_care_guide' або персоналу.
    """
    model = CareGuide
    form_class = CareGuideForm
    template_name = "catalog/careguide_form.html"
    permission_required = "catalog.can_manage_care_guide"

    def dispatch(self, request, *args, **kwargs):
        self.flower = get_object_or_404(Flower, pk=self.kwargs.get("flower_pk"))
        if hasattr(self.flower, "care_guide"):
            messages.info(request, f"Для квітки «{self.flower.name}» вже існує пам'ятка догляду.")
            return redirect("catalog:care_guide_detail", pk=self.flower.care_guide.pk)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.flower = self.flower
        form.instance.expert = self.request.user
        messages.success(self.request, f"Довідник догляду для «{self.flower.name}» успішно складено!")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["flower"] = self.flower
        return context


class OccasionListView(ListView):
    """
    В6.1: Список приводів для підбору букетів.
    """
    model = Occasion
    template_name = "catalog/occasion_list.html"
    context_object_name = "occasions"

    def get_queryset(self):
        return Occasion.objects.annotate(flower_count=Count("flowers"))


class OccasionDetailView(DetailView):
    """
    В6.1, В6.5 (slug): Сторінка підбору квітів до конкретного приводу.
    """
    model = Occasion
    template_name = "catalog/occasion_detail.html"
    context_object_name = "occasion"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["flowers"] = self.object.flowers.filter(
            in_stock=True
        ).select_related("category", "owner")
        return context


class CategoryDetailView(DetailView):
    """
    Сторінка перегляду квітів у вибраній категорії.
    """
    model = Category
    template_name = "catalog/category_detail.html"
    context_object_name = "category"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["flowers"] = self.object.flowers.select_related("category", "owner")
        return context


class FavoritesListView(LoginRequiredMixin, ListView):
    """
    Перегляд списку збережених квітів користувача.
    """
    model = Favorite
    template_name = "catalog/favorites_list.html"
    context_object_name = "favorites"
    paginate_by = 6

    def get_queryset(self):
        return Favorite.objects.filter(
            user=self.request.user
        ).select_related("flower__category", "flower__owner")


# ==============================================================================
# 4. АВТЕНТИФІКАЦІЯ ТА РОЛІ (В7.1, В7.4)
# ==============================================================================

def register_view(request):
    """
    В7.1: Реєстрація нового користувача (UserCreationForm).
    """
    if request.user.is_authenticated:
        return redirect("catalog:flower_list")

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(
                request,
                f"Вітаємо, {user.username}! Ваш обліковий запис успішно створено. Увійдіть у систему."
            )
            return redirect("catalog:login")
    else:
        form = UserRegistrationForm()

    return render(request, "catalog/auth/register.html", {"form": form})


class CustomLoginView(LoginView):
    """
    В7.1: Вхід у систему з повідомленням.
    """
    template_name = "catalog/auth/login.html"

    def form_valid(self, form):
        messages.success(self.request, f"Раді бачити Вас знову, {form.get_user().username}!")
        return super().form_valid(form)


class FloristDashboardView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """
    В7.4, В7.5: Спеціальний закритий кабінет флориста (привілейована роль).
    Доступ дозволено лише персоналу або учасникам групи 'Флористи'.
    Серверна перевірка доступу через test_func.
    """
    model = Flower
    template_name = "catalog/florist_dashboard.html"
    context_object_name = "flowers"

    def test_func(self):
        user = self.request.user
        return user.is_authenticated and (
            user.is_staff or user.groups.filter(name="Флористи").exists()
        )

    def handle_no_permission(self):
        messages.error(self.request, "Цей розділ доступний лише флористам та персоналу магазину.")
        return redirect("catalog:flower_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["out_of_stock_count"] = Flower.objects.filter(in_stock=False).count()
        context["care_guides_count"] = CareGuide.objects.count()
        context["category_analytics"] = Category.objects.annotate(
            count=Count("flowers"),
            avg_price=Avg("flowers__price")
        )
        return context
