from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from catalog.models import Flower, CareGuide, Category, Occasion
from catalog.validators import validate_phone_ua, validate_positive_price, validate_latin_name


class FlowerForm(forms.ModelForm):
    """
    ModelForm для створення та редагування квітки (В5.1, В5.3).
    - fields перелічені явно (без __all__).
    - Поле власника (owner) та дата створення виключені (присвоюються у view).
    """
    class Meta:
        model = Flower
        # В5.1: явний список полів
        fields = [
            "name",
            "latin_name",
            "category",
            "occasions",
            "description",
            "price",
            "in_stock",
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
            "price": forms.NumberInput(attrs={
                "class": "form-control",
                "step": "0.50",
                "placeholder": "0.00"
            }),
            "in_stock": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "difficulty_level": forms.Select(attrs={"class": "form-select"}),
            "image_url": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "https://images.unsplash.com/..."
            }),
        }

    # В5.3: метод clean_<field>() з повідомленнями про помилки українською
    def clean_name(self):
        name = self.cleaned_data.get("name", "").strip()
        if len(name) < 3:
            raise ValidationError(
                "Назва квітки повинна містити щонайменше 3 символи.",
                code="name_too_short"
            )
        return name

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price is not None and price <= 0:
            raise ValidationError(
                "Ціна квітки повинна бути додатною та більшою за 0 грн.",
                code="invalid_price"
            )
        return price

    # В5.3: метод загальної валідації clean()
    def clean(self):
        cleaned_data = super().clean()
        price = cleaned_data.get("price")
        category = cleaned_data.get("category")

        # Додаткова логічна валідація
        if category and "екзотичн" in category.name.lower() and price and price < 50:
            raise ValidationError(
                "Для екзотичних квітів мінімальна вартість не може бути нижчою за 50 грн.",
                code="exotic_price_too_low"
            )
        return cleaned_data


class CareGuideForm(forms.ModelForm):
    """
    ModelForm для укладання довідника з догляду (В5.1).
    Призначена для флористів та адміністраторів.
    """
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
    """
    В5.2: forms.Form, НЕ пов'язана з моделлю.
    Форма комплексного пошуку та фільтрації квітів у каталозі.
    """
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
    max_price = forms.DecimalField(
        required=False,
        label="Максимальна ціна (грн)",
        min_value=0,
        widget=forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "До грн"
        })
    )
    in_stock_only = forms.BooleanField(
        required=False,
        label="Лише в наявності",
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"})
    )


class FloristConsultationForm(forms.Form):
    """
    В5.2: forms.Form, НЕ пов'язана з моделлю.
    Форма запиту на консультацію або підбір авторського букета.
    """
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
    budget = forms.DecimalField(
        min_value=100,
        decimal_places=2,
        label="Орієнтовний бюджет (грн)",
        widget=forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "Від 300 грн"
        })
    )
    preferences = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "rows": 3,
            "placeholder": "Улюблені кольори, сорти, побажання щодо оформлення..."
        }),
        label="Побажання та деталі"
    )

    # В5.3: clean_<field>() валідатор
    def clean_budget(self):
        budget = self.cleaned_data.get("budget")
        if budget is not None and budget < 200:
            raise ValidationError(
                "Мінімальний бюджет для індивідуального авторського букета становить 200 грн.",
                code="budget_too_low"
            )
        return budget


class UserRegistrationForm(UserCreationForm):
    """
    Форма реєстрації нового користувача (В7.1)
    з розширеними полями та українізованим інтерфейсом.
    """
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
        fields = ("username", "first_name", "last_name", "email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault("class", "form-control")
