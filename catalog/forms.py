from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from catalog.models import Flower, CareGuide, Category, Occasion
from catalog.validators import validate_phone_ua, validate_latin_name


class FlowerForm(forms.ModelForm):

    class Meta:
        model = Flower
        fields = [
            "name",
            "latin_name",
            "category",
            "occasions",
            "description",
            "fun_fact",
            "difficulty_level",
            "image_url",
        ]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Наприклад: Півонія 'Сара Бернар'"
            }),
            "latin_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Наприклад: Paeonia lactiflora"
            }),
            "category": forms.Select(attrs={"class": "form-select"}),
            "occasions": forms.CheckboxSelectMultiple(attrs={"class": "form-check-input"}),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Опишіть особливості квітки, аромат, колористику..."
            }),
            "fun_fact": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 2,
                "placeholder": "Цікавий факт чи історія сорту..."
            }),
            "difficulty_level": forms.Select(attrs={"class": "form-select"}),
            "image_url": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "https://images.unsplash.com/..."
            }),
        }


    def clean_name(self):
        name = self.cleaned_data.get("name", "").strip()
        if len(name) < 3:
            raise ValidationError(
                "Назва квітки повинна містити щонайменше 3 символи.",
                code="name_too_short"
            )
        return name


class CareGuideForm(forms.ModelForm):

    class Meta:
        model = CareGuide
        fields = [
            "watering_frequency_days",
            "temperature_range",
            "light_requirement",
            "humidity_level",
            "stem_cutting_tips",
            "florist_secret",
        ]
        widgets = {
            "watering_frequency_days": forms.NumberInput(attrs={
                "class": "form-control",
                "min": "0"
            }),
            "temperature_range": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Наприклад: 18-22°C"
            }),
            "light_requirement": forms.Select(attrs={"class": "form-select"}),
            "humidity_level": forms.Select(attrs={"class": "form-select"}),
            "stem_cutting_tips": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Як підрізати стебла, яку воду наливати..."
            }),
            "florist_secret": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Порада від експерта для тривалого збереження..."
            }),
        }


class FlowerFilterForm(forms.Form):

    q = forms.CharField(
        required=False,
        label="Пошуковий запит",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Назва, латина або опис..."
        })
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        empty_label="— Всі категорії —",
        label="Категорія",
        widget=forms.Select(attrs={"class": "form-select"})
    )
    occasion = forms.ModelChoiceField(
        queryset=Occasion.objects.all(),
        required=False,
        empty_label="— Будь-який привід —",
        label="Привід / Подія",
        widget=forms.Select(attrs={"class": "form-select"})
    )


class CareGuideFilterForm(forms.Form):

    q = forms.CharField(
        required=False,
        label="Пошук",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Назва квітки або латина..."
        })
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        empty_label="— Всі категорії —",
        label="Категорія",
        widget=forms.Select(attrs={"class": "form-select"})
    )
    light = forms.ChoiceField(
        required=False,
        label="Освітлення",
        choices=[
            ("", "— Будь-яке освітлення —"),
            ("direct_sun", "Пряме сонце"),
            ("bright_indirect", "Яскраве розсіяне"),
            ("partial_shade", "Напівтінь"),
            ("shade", "Тінь"),
        ],
        widget=forms.Select(attrs={"class": "form-select"})
    )
    humidity = forms.ChoiceField(
        required=False,
        label="Вологість",
        choices=[
            ("", "— Будь-яка вологість —"),
            ("low", "Низька"),
            ("medium", "Помірна"),
            ("high", "Висока"),
        ],
        widget=forms.Select(attrs={"class": "form-select"})
    )


class FloristConsultationForm(forms.Form):

    client_name = forms.CharField(
        max_length=100,
        label="Ваше ім'я",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Олена або Богдан"
        })
    )
    phone = forms.CharField(
        max_length=20,
        validators=[validate_phone_ua],
        label="Номер телефону",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "+380501234567"
        })
    )
    email = forms.EmailField(
        label="Email для зв'язку",
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "name@example.com"
        })
    )
    occasion_description = forms.CharField(
        max_length=200,
        label="До якої події підбираємо квіти?",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Наприклад: Річниця весілля, 5 років"
        })
    )
    preferences = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "rows": 3,
            "placeholder": "Улюблені кольори, сорти, побажання щодо оформлення..."
        }),
        label="Побажання та деталі",
        required=False
    )


class UserRegistrationForm(UserCreationForm):

    ROLE_CHOICES = [
        ("client", "Клієнт (перегляд каталогу, додавання в обране, замовлення консультацій)"),
        ("florist", "Флорист (ведення довідників догляду, доступ до панелі флориста)"),
    ]

    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        initial="client",
        label="Оберіть вашу роль у системі",
        widget=forms.Select(attrs={"class": "form-select"})
    )
    email = forms.EmailField(
        required=True,
        label="Електронна пошта",
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "user@example.com"})
    )
    first_name = forms.CharField(
        required=True,
        label="Ім'я",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ваше ім'я"})
    )
    last_name = forms.CharField(
        required=True,
        label="Прізвище",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ваше прізвище"})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "first_name", "last_name", "email", "role")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault("class", "form-control")
        if "role" in self.fields:
            self.fields["role"].widget.attrs["class"] = "form-select"

    def save(self, commit=True):
        user = super().save(commit=commit)
        role = self.cleaned_data.get("role", "client")
        if commit:
            self._assign_role(user, role)
        return user

    def _assign_role(self, user, role):
        if role == "florist":
            group, _ = Group.objects.get_or_create(name="Флористи")
            user.groups.add(group)
        else:
            group, _ = Group.objects.get_or_create(name="Клієнти")
            user.groups.add(group)
