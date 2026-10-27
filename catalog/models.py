from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from catalog.validators import validate_latin_name


class Category(models.Model):
    category_id = models.AutoField(primary_key=True, db_column="category_id")
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
        db_table = "catalog_category"
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"
        ordering = ["name"]

    def __str__(self):
        return f"{self.icon_emoji} {self.name}"

    def get_absolute_url(self):
        return reverse("catalog:category_detail", kwargs={"slug": self.slug})


class Occasion(models.Model):

    SEASON_CHOICES = [
        ("all_year", "Цілий рік"),
        ("spring", "Весняний період"),
        ("summer", "Літній сезон"),
        ("autumn", "Осінній період"),
        ("winter", "Зимові свята"),
    ]

    occasion_id = models.AutoField(primary_key=True, db_column="occasion_id")
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
        db_table = "catalog_occasion"
        verbose_name = "Привід / Подія"
        verbose_name_plural = "Приводи та події"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("catalog:occasion_detail", kwargs={"slug": self.slug})


class Flower(models.Model):
    DIFFICULTY_CHOICES = [
        ("easy", "Невибаглива (легко)"),
        ("medium", "Середня складність"),
        ("hard", "Вимоглива до умов"),
    ]
    flower_id = models.AutoField(primary_key=True, db_column="flower_id")
    name = models.CharField(max_length=150, verbose_name="Назва квітки")
    latin_name = models.CharField(max_length=150, blank=True, validators=[validate_latin_name], verbose_name="Ботанічна (латинська) назва")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="flowers", db_column="category_id", verbose_name="Категорія")
    occasions = models.ManyToManyField(Occasion, related_name="flowers", blank=True, db_table="catalog_flower_occasions", verbose_name="Рекомендовані події")
    description = models.TextField(verbose_name="Опис, символізм та флористичне значення")
    fun_fact = models.TextField(blank=True, verbose_name="Цікавий факт / коротка історія")
    difficulty_level = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, default="easy", verbose_name="Складність догляду")
    image_url = models.URLField(max_length=2000, blank=True, default="https://plus.unsplash.com/premium_photo-1676475964992-6404b8db0b53?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D", verbose_name="URL фотографії")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата додавання")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="flowers", db_column="owner_id", verbose_name="Автор запису")
    class Meta:
        db_table = "catalog_flower"
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
        return reverse("catalog:flower_detail", kwargs={"pk": self.pk})


class CareGuide(models.Model):

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


    careguide_id = models.AutoField(primary_key=True, db_column="careguide_id")
    flower = models.OneToOneField(
        Flower,
        on_delete=models.CASCADE,
        related_name="care_guide",
        db_column="flower_id",
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
    soil_type = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Рекомендований тип ґрунту (для горщикових рослин)"
    )
    fun_fact = models.TextField(
        blank=True,
        verbose_name="Цікавий факт про рослину"
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

    expert = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="authored_guides",
        db_column="expert_id",
        verbose_name="Експерт-укладач"
    )

    class Meta:
        db_table = "catalog_careguide"
        verbose_name = "Довідник з догляду"
        verbose_name_plural = "Довідники з догляду"
        ordering = ["flower__name"]

    def __str__(self):
        return f"Пам'ятка догляду: {self.flower.name}"

    def get_absolute_url(self):
        return reverse("catalog:care_guide_detail", kwargs={"pk": self.pk})


class Favorite(models.Model):
    favorite_id = models.AutoField(primary_key=True, db_column="favorite_id")
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="favorites",
        db_column="user_id",
        verbose_name="Користувач"
    )
    flower = models.ForeignKey(
        Flower,
        on_delete=models.CASCADE,
        related_name="favorited_by",
        db_column="flower_id",
        verbose_name="Квітка"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Час збереження"
    )

    class Meta:
        db_table = "catalog_favorite"
        verbose_name = "Обрана квітка"
        verbose_name_plural = "Обрані квіти"
        ordering = ["-created_at"]
        
        constraints = [
            models.UniqueConstraint(
                fields=["user", "flower"],
                name="unique_user_flower_favorite"
            )
        ]

    def __str__(self):
        return f"{self.user.username} ❤️ {self.flower.name}"


class ConsultationRequest(models.Model):
 
    STATUS_CHOICES = [
        ("new", "Новий запит"),
        ("in_progress", "В обробці"),
        ("completed", "Завершено"),
        ("cancelled", "Скасовано"),
    ]

    consultation_id = models.AutoField(primary_key=True, db_column="consultation_id")
    client_name = models.CharField(
        max_length=100,
        verbose_name="Ім'я клієнта"
    )
    phone = models.CharField(
        max_length=20,
        verbose_name="Номер телефону"
    )
    email = models.EmailField(
        verbose_name="Email для зв'язку"
    )
    occasion_description = models.CharField(
        max_length=200,
        verbose_name="До якої події"
    )
    preferences = models.TextField(
        blank=True,
        verbose_name="Побажання та деталі"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="new",
        verbose_name="Статус запиту"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата та час запиту"
    )

    class Meta:
        db_table = "catalog_consultationrequest"
        verbose_name = "Запит на консультацію"
        verbose_name_plural = "Запити на консультації"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Запит #{self.pk} від {self.client_name} ({self.created_at.strftime('%d.%m.%Y %H:%M')})"
