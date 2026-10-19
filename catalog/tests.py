from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User, Group, Permission
from django.core.exceptions import ValidationError
from decimal import Decimal

from catalog.models import Category, Occasion, Flower, CareGuide, Favorite
from catalog.validators import validate_positive_price, validate_latin_name, validate_phone_ua


class FloristDomainModelTests(TestCase):
    """
    Тести для моделей власного домену (В3.1, В3.2, Д1, Д2, Д3).
    """
    def setUp(self):
        self.user, _ = User.objects.get_or_create(username="testuser_unique")
        self.category, _ = Category.objects.get_or_create(
            slug="test-cut-flowers",
            defaults={
                "name": "Тестові зрізані квіти",
                "description": "Свіжі квіти для тестів",
                "icon_emoji": "🌹"
            }
        )
        self.occasion, _ = Occasion.objects.get_or_create(
            slug="test-wedding",
            defaults={
                "name": "Тестове весілля",
                "description": "Для наречених",
                "season": "all_year"
            }
        )
        self.flower, _ = Flower.objects.get_or_create(
            name="Унікальна Троянда Ель Торо",
            defaults={
                "latin_name": "Rosa El Toro",
                "category": self.category,
                "description": "Яскрава гофрована троянда",
                "price": Decimal("75.00"),
                "in_stock": True,
                "difficulty_level": "easy",
                "owner": self.user
            }
        )
        self.flower.occasions.add(self.occasion)

        self.care_guide, _ = CareGuide.objects.get_or_create(
            flower=self.flower,
            defaults={
                "watering_frequency_days": 2,
                "temperature_range": "18-20°C",
                "light_requirement": "bright_indirect",
                "humidity_level": "medium",
                "stem_cutting_tips": "Підрізати гострим ножем під кутом 45 градусів.",
                "florist_secret": "Міняти воду щодня.",
                "expert": self.user
            }
        )

    def test_model_str_methods(self):
        """В3.2: Перевірка __str__() у кожній моделі."""
        self.assertEqual(str(self.category), "🌹 Тестові зрізані квіти")
        self.assertEqual(str(self.occasion), "Тестове весілля")
        self.assertEqual(str(self.flower), "Унікальна Троянда Ель Торо (Тестові зрізані квіти)")
        self.assertEqual(str(self.care_guide), "Пам'ятка догляду: Унікальна Троянда Ель Торо")

    def test_get_absolute_url(self):
        """В6.3: Перевірка get_absolute_url() у моделях."""
        self.assertEqual(self.flower.get_absolute_url(), f"/flowers/{self.flower.pk}/")
        self.assertEqual(self.care_guide.get_absolute_url(), f"/care-guides/{self.care_guide.pk}/")

    def test_favorite_unique_constraint(self):
        """Д3: Перевірка UniqueConstraint для моделі Favorite."""
        Favorite.objects.filter(user=self.user, flower=self.flower).delete()
        Favorite.objects.create(user=self.user, flower=self.flower)
        with self.assertRaises(Exception):
            Favorite.objects.create(user=self.user, flower=self.flower)

    def test_validators(self):
        """В5.3: Перевірка власних валідаторів."""
        # Ціна повинна бути більше 0
        with self.assertRaises(ValidationError):
            validate_positive_price(Decimal("-10.00"))
        with self.assertRaises(ValidationError):
            validate_positive_price(Decimal("0.00"))

        # Латинська назва
        with self.assertRaises(ValidationError):
            validate_latin_name("Троянда 123")

        # Номер телефону України
        with self.assertRaises(ValidationError):
            validate_phone_ua("12345")
        # Коректний номер
        validate_phone_ua("+380501234567")


class FloristViewsAndSecurityTests(TestCase):
    """
    Тести для представлень, безпеки, доступу та ролей (В6, В7, В8).
    """
    def setUp(self):
        self.client = Client()
        self.user, _ = User.objects.get_or_create(username="unique_client1")
        self.user.set_password("pass12345")
        self.user.save()

        self.florist, _ = User.objects.get_or_create(username="unique_florist1", is_staff=True)
        self.florist.set_password("pass12345")
        self.florist.save()

        florist_group, _ = Group.objects.get_or_create(name="Флористи")
        perm = Permission.objects.filter(codename="can_manage_care_guide").first()
        if perm:
            florist_group.permissions.add(perm)
        self.florist.groups.add(florist_group)

        self.category, _ = Category.objects.get_or_create(
            slug="view-test-category",
            defaults={"name": "Категорія для тестів", "icon_emoji": "🌸"}
        )
        self.flower, _ = Flower.objects.get_or_create(
            name="Унікальна Гвоздика Шабо",
            defaults={
                "latin_name": "Dianthus caryophyllus",
                "category": self.category,
                "description": "Опис унікальної гвоздики для перевірки",
                "price": Decimal("150.00"),
                "in_stock": True,
                "owner": self.florist
            }
        )
        self.admin, _ = User.objects.get_or_create(username="superadmin_test")
        self.admin.is_superuser = True
        self.admin.is_staff = True
        self.admin.set_password("admin12345")
        self.admin.save()

    def test_home_view(self):
        """В6.2: Перевірка головної сторінки (FBV) та агрегатної статистики."""
        response = self.client.get(reverse("catalog:home"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("stats", response.context)
        self.assertGreaterEqual(response.context["stats"]["total_flowers"], 1)

    def test_flower_list_view_and_filtering(self):
        """В6.1, Д4: Перевірка каталогу та фільтрації через Q-об'єкти."""
        response = self.client.get(reverse("catalog:flower_list"), {"q": "Унікальна Гвоздика"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["flowers"]), 1)

        response_empty = self.client.get(reverse("catalog:flower_list"), {"q": "НеіснуючаКвіткаXYZ123"})
        self.assertEqual(len(response_empty.context["flowers"]), 0)

    def test_flower_detail_view(self):
        """В6.1, В6.5: Детальна сторінка квітки з конвертером <int:pk>."""
        url = reverse("catalog:flower_detail", kwargs={"pk": self.flower.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Унікальна Гвоздика Шабо")

    def test_flower_create_login_required(self):
        """В7.3: Створення недоступне для неавторизованих."""
        url = reverse("catalog:flower_create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("catalog:login"), response.url)

    def test_client_cannot_create_flower(self):
        """Тільки адміністратор може додавати нові квіти: клієнт отримує відмову."""
        self.client.login(username="unique_client1", password="pass12345")
        url = reverse("catalog:flower_create")
        response = self.client.get(url)
        # Перенаправлення на каталог із забороною
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("catalog:flower_list"))

    def test_flower_create_by_admin(self):
        """В7.2: Адміністратор успішно створює квітку, автор присвоюється у form_valid()."""
        self.client.login(username="superadmin_test", password="admin12345")
        data = {
            "name": "Нова тестувальна квітка",
            "latin_name": "Tulipa gesneriana",
            "category": self.category.pk,
            "description": "Гарний весняний тюльпан для тестів",
            "price": "60.00",
            "in_stock": True,
            "difficulty_level": "easy",
            "image_url": "https://images.unsplash.com/photo-1520763185298-1b434c919102",
        }
        response = self.client.post(reverse("catalog:flower_create"), data)
        self.assertEqual(response.status_code, 302)
        created_flower = Flower.objects.get(name="Нова тестувальна квітка")
        self.assertEqual(created_flower.owner, self.admin)

    def test_prevent_editing_other_user_record(self):
        """В7.3, В7.5: Заборона редагування чужого запису звичайним користувачем."""
        self.client.login(username="unique_client1", password="pass12345")
        url = reverse("catalog:flower_update", kwargs={"pk": self.flower.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_florist_dashboard_restricted_access(self):
        """В7.4, В7.5: Панель флориста недоступна звичайному користувачу."""
        self.client.login(username="unique_client1", password="pass12345")
        response = self.client.get(reverse("catalog:florist_dashboard"))
        self.assertEqual(response.status_code, 302)

        # Доступна для флориста
        self.client.login(username="unique_florist1", password="pass12345")
        response_florist = self.client.get(reverse("catalog:florist_dashboard"))
        self.assertEqual(response_florist.status_code, 200)

    def test_toggle_favorite_post_only(self):
        """В5.4, В6.2: Додавання в обране виключно через POST з PRG."""
        self.client.login(username="unique_client1", password="pass12345")
        url = reverse("catalog:toggle_favorite", kwargs={"pk": self.flower.pk})
        
        # GET заборонено
        response_get = self.client.get(url)
        self.assertEqual(response_get.status_code, 405)

        # POST дозволено
        response_post = self.client.post(url)
        self.assertEqual(response_post.status_code, 302)
        self.assertTrue(Favorite.objects.filter(user=self.user, flower=self.flower).exists())

    def test_middleware_timing_header(self):
        """Д7: Перевірка роботи власного middleware та заголовка часу."""
        response = self.client.get(reverse("catalog:home"))
        self.assertIn("X-Response-Time-ms", response.headers)
