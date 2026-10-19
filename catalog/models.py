from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from catalog.validators import validate_positive_price, validate_latin_name


class Category(models.Model):
    """
    Модель 1: Категорія квітів (В3.1, В3.2, Д3).
    Приклади: Зрізані квіти, Кімнатні рослини, Екзотичні квіти, Зелень для букетів.
    """
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Назва категорії"
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name="URL-ідентифікатор (slug)"
    )
    description = models.TextField(
        blank=True,
        verbose_name="Опис категорії"
    )
    icon_emoji = models.CharField(
        max_length=10,
        default="🌸",
        verbose_name="Емодзі-іконка"
    )

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"
        ordering = ["name"]

    def __str__(self):
        return f"{self.icon_emoji} {self.name}"

    def get_absolute_url(self):
        return reverse("catalog:category_detail", kwargs={"slug": self.slug})


class Occasion(models.Model):
    """
    Модель 2: Привід / Подія для флористичного підбору (В3.1, В3.2, Д1, Д3).
    Приклади: Весілля, День народження, Романтичне побачення, День матері, Офіційне привітання.
    """
    SEASON_CHOICES = [
        ("all_year", "Цілий рік"),
        ("spring", "Весняний період"),
        ("summer", "Літній сезон"),
        ("autumn", "Осінній період"),
        ("winter", "Зимові свята"),
    ]

    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Назва приводу"
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name="URL-ідентифікатор (slug)"
    )
    description = models.TextField(
        blank=True,
        verbose_name="Опис рекомендацій для події"
    )
    season = models.CharField(
        max_length=20,
        choices=SEASON_CHOICES,
        default="all_year",
        verbose_name="Сезонність"
    )
    badge_color = models.CharField(
        max_length=30,
        default="danger",
        verbose_name="Колір бейджа (Bootstrap)"
    )

    class Meta:
        verbose_name = "Привід / Подія"
        verbose_name_plural = "Приводи та події"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("catalog:occasion_detail", kwargs={"slug": self.slug})


class Flower(models.Model):
    """
    Модель 3 (Основна сутність): Квітка (В3.1, В3.2, В6.3, Д1, Д2, Д3, Д6).
    Пов'язана з Category (ForeignKey), Occasion (ManyToManyField) та User (власник/автор).
    """
    DIFFICULTY_CHOICES = [
        ("easy", "Невибаглива (легко)"),
        ("medium", "Середня складність"),
        ("hard", "Вимоглива до умов"),
    ]

    name = models.CharField(
        max_length=150,
        verbose_name="Назва квітки"
    )
    latin_name = models.CharField(
        max_length=150,
        blank=True,
        validators=[validate_latin_name],
        verbose_name="Ботанічна (латинська) назва"
    )
    # Д2: on_delete=models.PROTECT — категорію не можна видалити, якщо в ній є квіти.
    # Це захищає каталог від випадкової втрати класифікації.
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="flowers",
        verbose_name="Категорія"
    )
    # Д1: ManyToManyField з related_name для швидкого зворотного доступу occasion.flowers.all()
    occasions = models.ManyToManyField(
        Occasion,
        related_name="flowers",
        blank=True,
        verbose_name="Рекомендовані події"
    )
    description = models.TextField(
        verbose_name="Опис, символізм та флористичне значення"
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[validate_positive_price],
        verbose_name="Орієнтовна ціна (грн/шт)"
    )
    in_stock = models.BooleanField(
        default=True,
        verbose_name="Є в наявності в майстерні"
    )
    difficulty_level = models.CharField(
        max_length=20,
        choices=DIFFICULTY_CHOICES,
        default="easy",
        verbose_name="Складність догляду"
    )
    image_url = models.URLField(
        max_length=500,
        default="https://images.unsplash.com/photo-1563245372-f21724e3856d?auto=format&fit=crop&w=800&q=80",
        verbose_name="URL фотографії"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата додавання"
    )
    # В3.1, Д2: on_delete=models.CASCADE — при видаленні користувача його створені записи видаляються.
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="flowers",
        verbose_name="Автор запису"
    )

    class Meta:
        verbose_name = "Квітка"
        verbose_name_plural = "Квіти"
        ordering = ["-created_at"]
        permissions = [
            ("can_publish_catalog", "Може публікувати квіти у вітрину каталогу"),
            ("can_manage_care_guide", "Може складати та редагувати довідники догляду"),
        ]

    def __str__(self):
        return f"{self.name} ({self.category.name})"

    def get_absolute_url(self):
        # В6.3: get_absolute_url() у моделі
        return reverse("catalog:flower_detail", kwargs={"pk": self.pk})


class CareGuide(models.Model):
    """
    Модель 4: Довідник з догляду за квіткою (В3.1, В3.2, Д2, Д3).
    Зв'язок OneToOne з Flower та ForeignKey на експерта-флориста (User).
    """
    LIGHT_CHOICES = [
        ("direct_sun", "Пряме сонячне світло"),
        ("bright_indirect", "Яскраве розсіяне світло"),
        ("partial_shade", "Напівтінь"),
        ("shade", "Тінь"),
    ]

    HUMIDITY_CHOICES = [
        ("low", "Низька (до 40%)"),
        ("medium", "Помірна (40-60%)"),
        ("high", "Висока (понад 60%)"),
    ]

    # Д2: on_delete=models.CASCADE — довідник нерозривно пов'язаний із квіткою.
    # Якщо квітку видалено, її довідник також видаляється.
    flower = models.OneToOneField(
        Flower,
        on_delete=models.CASCADE,
        related_name="care_guide",
        verbose_name="Квітка"
    )
    watering_frequency_days = models.PositiveIntegerField(
        default=2,
        verbose_name="Частота заміни води / поливу (днів)"
    )
    temperature_range = models.CharField(
        max_length=50,
        default="18-22°C",
        verbose_name="Оптимальний температурний режим"
    )
    light_requirement = models.CharField(
        max_length=30,
        choices=LIGHT_CHOICES,
        default="bright_indirect",
        verbose_name="Вимоги до освітлення"
    )
    humidity_level = models.CharField(
        max_length=20,
        choices=HUMIDITY_CHOICES,
        default="medium",
        verbose_name="Рівень вологості"
    )
    stem_cutting_tips = models.TextField(
        verbose_name="Правила підрізання стебел і підготовки води"
    )
    florist_secret = models.TextField(
        blank=True,
        verbose_name="Професійний секрет флориста для стійкості"
    )
    updated_at = models.DateField(
        auto_now=True,
        verbose_name="Дата оновлення довідника"
    )
    # Д2: on_delete=models.SET_NULL — якщо обліковий запис флориста видалено,
    # корисна інструкція зберігається в довіднику.
    expert = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="authored_guides",
        verbose_name="Експерт-укладач"
    )

    class Meta:
        verbose_name = "Довідник з догляду"
        verbose_name_plural = "Довідники з догляду"
        ordering = ["flower__name"]

    def __str__(self):
        return f"Пам'ятка догляду: {self.flower.name}"

    def get_absolute_url(self):
        return reverse("catalog:care_guide_detail", kwargs={"pk": self.pk})


class Favorite(models.Model):
    """
    Модель 5: Список обраних квітів користувача (В3.1, Д3).
    Зв'язок між User та Flower із UniqueConstraint, щоб уникнути дублікатів.
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="favorites",
        verbose_name="Користувач"
    )
    flower = models.ForeignKey(
        Flower,
        on_delete=models.CASCADE,
        related_name="favorited_by",
        verbose_name="Квітка"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Час збереження"
    )

    class Meta:
        verbose_name = "Обрана квітка"
        verbose_name_plural = "Обрані квіти"
        ordering = ["-created_at"]
        # Д3: UniqueConstraint для запобігання повторному додаванню однієї квітки
        constraints = [
            models.UniqueConstraint(
                fields=["user", "flower"],
                name="unique_user_flower_favorite"
            )
        ]

    def __str__(self):
        return f"{self.user.username} ❤️ {self.flower.name}"
