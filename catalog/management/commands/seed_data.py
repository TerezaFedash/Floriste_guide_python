from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group, Permission
from catalog.models import Category, Occasion, Flower, CareGuide, Favorite
from catalog.seed_flowers_data import FLOWERS_DATA


class Command(BaseCommand):
    help = "Наповнює базу даних категоріями, нагодами, сортами квітів та довідниками догляду"

    def handle(self, *args, **options):
        self.stdout.write("Початок наповнення бази даних...")

        # 1. Групи
        florist_group, _ = Group.objects.get_or_create(name="Флористи")
        client_group, _ = Group.objects.get_or_create(name="Клієнти")

        # 2. Користувачі
        admin_user = User.objects.filter(username="admin").first()
        if not admin_user:
            admin_user = User.objects.create_superuser(
                username="admin",
                email="admin@florist.ua",
                password="admin12345",
                first_name="Адміністратор",
                last_name="Системи"
            )
            self.stdout.write("Створено адміністратора: admin")

        florist_user = User.objects.filter(username="olena_florist").first()
        if not florist_user:
            florist_user = User.objects.create_user(
                username="olena_florist",
                email="olena@florist.ua",
                password="florist12345",
                first_name="Олена",
                last_name="Квіткова",
                is_staff=True
            )
            florist_user.groups.add(florist_group)
            self.stdout.write("Створено флориста: olena_florist")

        client_user = User.objects.filter(username="ivan_client").first()
        if not client_user:
            client_user = User.objects.create_user(
                username="ivan_client",
                email="ivan@gmail.com",
                password="client12345",
                first_name="Іван",
                last_name="Покупченко"
            )
            client_user.groups.add(client_group)
            self.stdout.write("Створено клієнта: ivan_client")

        # 3. Категорії
        cat_cut, _ = Category.objects.get_or_create(
            slug="cut-flowers",
            defaults={
                "name": "Зрізані квіти",
                "description": "Свіжозрізані сортові квіти для авторських букетів, композицій та декорування інтер'єру.",
                "icon_emoji": "🌹",
            }
        )
        cat_indoor, _ = Category.objects.get_or_create(
            slug="indoor-plants",
            defaults={
                "name": "Кімнатні рослини",
                "description": "Горщикові декоративно-листяні та квітучі рослини для створення домашнього затишку.",
                "icon_emoji": "🪴",
            }
        )
        cat_dried, _ = Category.objects.get_or_create(
            slug="dried-flowers",
            defaults={
                "name": "Сухоцвіти",
                "description": "Довговічні стабілізовані квіти, польові сухоцвіти та трави, що не в'януть роками.",
                "icon_emoji": "🌾",
            }
        )
        cat_exotic, _ = Category.objects.get_or_create(
            slug="exotic-flowers",
            defaults={
                "name": "Екзотичні квіти",
                "description": "Рідкісні види орхідей, тропічні суцвіття та унікальні ботанічні форми.",
                "icon_emoji": "🌺",
            }
        )

        categories_by_slug = {
            "cut-flowers": cat_cut,
            "indoor-plants": cat_indoor,
            "dried-flowers": cat_dried,
            "exotic-flowers": cat_exotic,
        }

        # 4. Нагоди
        occ_wedding, _ = Occasion.objects.get_or_create(
            slug="wedding",
            defaults={
                "name": "Весілля",
                "description": "Ніжні пастельні тони для букета нареченої та оформлення урочистостей.",
                "season": "all_year",
                "badge_color": "secondary",
            }
        )
        occ_bday, _ = Occasion.objects.get_or_create(
            slug="birthday",
            defaults={
                "name": "День народження",
                "description": "Яскраві, радісні композиції для щирих побажань гарного настрою.",
                "season": "all_year",
                "badge_color": "info",
            }
        )
        occ_romance, _ = Occasion.objects.get_or_create(
            slug="romance",
            defaults={
                "name": "Романтичне побачення",
                "description": "Чуттєві аромати та ніжні відтінки для вираження щирого кохання.",
                "season": "all_year",
                "badge_color": "danger",
            }
        )
        occ_mom, _ = Occasion.objects.get_or_create(
            slug="mothers-day",
            defaults={
                "name": "День матері",
                "description": "Зворушливі весняні квіти та теплі композиції для найрідніших мам.",
                "season": "spring",
                "badge_color": "success",
            }
        )
        occ_business, _ = Occasion.objects.get_or_create(
            slug="business",
            defaults={
                "name": "Діловий протокол",
                "description": "Стримані, елегантні композиції у вертикальному стилі для колег і партнерів.",
                "season": "all_year",
                "badge_color": "dark",
            }
        )

        occasions_by_slug = {
            "wedding": occ_wedding,
            "birthday": occ_bday,
            "romance": occ_romance,
            "mothers-day": occ_mom,
            "business": occ_business,
        }

        # 5. Квіти та довідники догляду
        count_created = 0
        for item in FLOWERS_DATA:
            cat = categories_by_slug.get(item["category_slug"])
            if not cat:
                continue

            flower, created = Flower.objects.get_or_create(
                name=item["name"],
                defaults={
                    "latin_name": item["latin_name"],
                    "category": cat,
                    "description": item["description"],
                    "fun_fact": item.get("fun_fact", ""),
                    "difficulty_level": item["difficulty_level"],
                    "image_url": item["image_url"],
                    "owner": admin_user,
                }
            )

            if created:
                count_created += 1
                for occ_slug in item.get("occasions", []):
                    occ_obj = occasions_by_slug.get(occ_slug)
                    if occ_obj:
                        flower.occasions.add(occ_obj)

                care = item.get("care", {})
                if care:
                    CareGuide.objects.get_or_create(
                        flower=flower,
                        defaults={
                            "watering_frequency_days": care.get("watering_frequency_days", 2),
                            "temperature_range": care.get("temperature_range", "18-22°C"),
                            "light_requirement": care.get("light_requirement", "bright_indirect"),
                            "humidity_level": care.get("humidity_level", "medium"),
                            "soil_type": care.get("soil_type", ""),
                            "stem_cutting_tips": care.get("stem_cutting_tips", ""),
                            "florist_secret": care.get("florist_secret", ""),
                            "fun_fact": care.get("fun_fact", ""),
                            "expert": florist_user,
                        }
                    )

        # 6. Обране
        f_rose = Flower.objects.filter(name="Троянда").first()
        f_peony = Flower.objects.filter(name="Півонія").first()
        if f_rose and client_user:
            Favorite.objects.get_or_create(user=client_user, flower=f_rose)
        if f_peony and client_user:
            Favorite.objects.get_or_create(user=client_user, flower=f_peony)

        self.stdout.write(self.style.SUCCESS(
            f"Успішно! Завантажено {Flower.objects.count()} квітів у {Category.objects.count()} категоріях!"
        ))
