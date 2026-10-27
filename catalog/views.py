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

from catalog.models import Category, Occasion, Flower, CareGuide, Favorite, ConsultationRequest
from catalog.forms import (
    FlowerForm,
    CareGuideForm,
    FlowerFilterForm,
    CareGuideFilterForm,
    FloristConsultationForm,
    UserRegistrationForm,
)


def home_view(request):
    
    stats = Flower.objects.aggregate(
        total_flowers=Count("pk"),
    )

    categories_with_counts = Category.objects.annotate(
        flower_count=Count("flowers")
    ).filter(flower_count__gt=0)
  
    featured_flowers = Flower.objects.select_related(
        "category", "owner"
    ).prefetch_related("occasions")[:4]

    occasions = Occasion.objects.all()[:6]

    context = {
        "stats": stats,
        "categories_with_counts": categories_with_counts,
        "featured_flowers": featured_flowers,
        "occasions": occasions,
    }
    return render(request, "catalog/home.html", context)


def consultation_view(request):
   
    if request.method == "POST":
        form = FloristConsultationForm(request.POST)
        if form.is_valid():
            client_name = form.cleaned_data["client_name"]
            phone = form.cleaned_data["phone"]
            email = form.cleaned_data["email"]
            occasion = form.cleaned_data["occasion_description"]
            preferences = form.cleaned_data.get("preferences", "")

           
            ConsultationRequest.objects.create(
                client_name=client_name,
                phone=phone,
                email=email,
                occasion_description=occasion,
                preferences=preferences,
            )

            messages.success(
                request,
                f"Дякуємо, {client_name}! Ваш запит на підбір квітів до події «{occasion}» "
                f"успішно збережено в системі та передано флористу. Ми зв'яжемося з Вами найближчим часом!"
            )
            return redirect("catalog:consultation")
    else:
        form = FloristConsultationForm()

    return render(request, "catalog/consultation.html", {"form": form})


@login_required
@require_POST
def toggle_favorite_view(request, pk):
   
    flower = get_object_or_404(Flower, pk=pk)
    fav_obj = Favorite.objects.filter(user=request.user, flower=flower).first()

    if fav_obj:
        fav_obj.delete()
        messages.info(request, f"Квітку «{flower.name}» видалено з Вашого обраного.")
    else:
        Favorite.objects.create(user=request.user, flower=flower)
        messages.success(request, f"Квітку «{flower.name}» успішно додано до обраного! 🌸")

   
    next_url = request.POST.get("next")
    if next_url and next_url.startswith("/"):
        return redirect(next_url)
    return redirect("catalog:flower_detail", pk=flower.pk)



class FlowerListView(ListView):

    model = Flower
    template_name = "catalog/flower_list.html"
    context_object_name = "flowers"
    paginate_by = 6

    def get_queryset(self):
        
        qs = Flower.objects.select_related("category", "owner").prefetch_related("occasions")

        
        self.filter_form = FlowerFilterForm(self.request.GET)
        if self.filter_form.is_valid():
            q = self.filter_form.cleaned_data.get("q")
            category = self.filter_form.cleaned_data.get("category")
            occasion = self.filter_form.cleaned_data.get("occasion")

            
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

        return qs.distinct()

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context["filter_form"] = self.filter_form
        context["total_found"] = self.get_queryset().count()
        return context


class FlowerDetailView(DetailView):
    
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
        
        context["related_flowers"] = Flower.objects.filter(
            category=flower.category
        ).exclude(pk=flower.pk)[:3]
        return context


class FlowerCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
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
        form.instance.owner = self.request.user
        messages.success(self.request, f"Квітку «{form.instance.name}» успішно додано до каталогу адміністратором!")
        return super().form_valid(form)


class OwnerOrStaffRequiredMixin(UserPassesTestMixin):
   
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
   
    model = Flower
    form_class = FlowerForm
    template_name = "catalog/flower_form.html"

    def form_valid(self, form):
        messages.success(self.request, f"Дані квітки «{form.instance.name}» успішно оновлено!")
        return super().form_valid(form)


class FlowerDeleteView(LoginRequiredMixin, OwnerOrStaffRequiredMixin, DeleteView):
    
    model = Flower
    template_name = "catalog/flower_confirm_delete.html"
    success_url = reverse_lazy("catalog:flower_list")

    def form_valid(self, form):
        flower_name = self.object.name
        response = super().form_valid(form)
        messages.warning(self.request, f"Квітку «{flower_name}» було успішно видалено з бази даних.")
        return response




class CareGuideListView(ListView):

    model = CareGuide
    template_name = "catalog/careguide_list.html"
    context_object_name = "guides"
    paginate_by = 6

    def get_queryset(self):
        qs = CareGuide.objects.select_related(
            "flower", "flower__category", "expert"
        ).order_by("flower__name")

        self.filter_form = CareGuideFilterForm(self.request.GET)
        if self.filter_form.is_valid():
            q = self.filter_form.cleaned_data.get("q")
            category = self.filter_form.cleaned_data.get("category")
            light = self.filter_form.cleaned_data.get("light")
            humidity = self.filter_form.cleaned_data.get("humidity")

            if q:
                qs = qs.filter(
                    Q(flower__name__icontains=q)
                    | Q(flower__latin_name__icontains=q)
                )
            if category:
                qs = qs.filter(flower__category=category)
            if light:
                qs = qs.filter(light_requirement=light)
            if humidity:
                qs = qs.filter(humidity_level=humidity)
        else:
            self.filter_form = CareGuideFilterForm()

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not hasattr(self, "filter_form"):
            self.filter_form = CareGuideFilterForm()
        context["filter_form"] = self.filter_form
        context["total_found"] = self.get_queryset().count()
        return context


class CareGuideDetailView(DetailView):
   
    model = CareGuide
    template_name = "catalog/careguide_detail.html"
    context_object_name = "guide"

    def get_queryset(self):
        return CareGuide.objects.select_related("flower", "expert")


class CareGuideCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
   
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
    
    model = Occasion
    template_name = "catalog/occasion_list.html"
    context_object_name = "occasions"

    def get_queryset(self):
        return Occasion.objects.annotate(flower_count=Count("flowers"))


class OccasionDetailView(DetailView):
    
    model = Occasion
    template_name = "catalog/occasion_detail.html"
    context_object_name = "occasion"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["flowers"] = self.object.flowers.select_related("category", "owner")
        return context


class CategoryDetailView(DetailView):
   
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
    
    model = Favorite
    template_name = "catalog/favorites_list.html"
    context_object_name = "favorites"
    paginate_by = 6

    def get_queryset(self):
        return Favorite.objects.filter(
            user=self.request.user
        ).select_related("flower__category", "flower__owner")




def register_view(request):

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
   
    template_name = "catalog/auth/login.html"

    def form_valid(self, form):
        messages.success(self.request, f"Раді бачити Вас знову, {form.get_user().username}!")
        return super().form_valid(form)


class FloristDashboardView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    
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
        context["care_guides_count"] = CareGuide.objects.count()
        context["consultation_requests"] = ConsultationRequest.objects.all()[:10]
        context["new_consultations_count"] = ConsultationRequest.objects.filter(status="new").count()
        context["category_analytics"] = Category.objects.annotate(
            count=Count("flowers")
        )
        return context
