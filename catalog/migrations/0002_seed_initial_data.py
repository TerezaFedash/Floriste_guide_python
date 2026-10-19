from django.db import migrations


def seed_data(apps, schema_editor):
    User = apps.get_model("auth", "User")
    Group = apps.get_model("auth", "Group")
    Permission = apps.get_model("auth", "Permission")
    Category = apps.get_model("catalog", "Category")
    Occasion = apps.get_model("catalog", "Occasion")
    Flower = apps.get_model("catalog", "Flower")
    CareGuide = apps.get_model("catalog", "CareGuide")
    Favorite = apps.get_model("catalog", "Favorite")

    # 1. Створення груп та ролей (Д6, В7.4)
    florist_group, _ = Group.objects.get_or_create(name="Флористи")
    client_group, _ = Group.objects.get_or_create(name="Клієнти")

    # Додавання прав групі "Флористи"
    care_perm = Permission.objects.filter(codename="can_manage_care_guide").first()
    if care_perm:
        florist_group.permissions.add(care_perm)
    catalog_perm = Permission.objects.filter(codename="can_publish_catalog").first()
    if catalog_perm:
        florist_group.permissions.add(catalog_perm)

    # 2. Створення демонстраційних користувачів (В3.5, В7.1)
    admin_user = User.objects.filter(username="admin").first()
    if not admin_user:
        admin_user = User.objects.create_superuser(
            username="admin",
            email="admin@florist.ua",
            password="admin12345",
            first_name="Адміністратор",
            last_name="Системи"
        )

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

    # 3. Створення категорій (В3.1, В3.5)
    cat_cut = Category.objects.create(
        name="Зрізані квіти",
        slug="cut-flowers",
        description="Свіжозрізані сортові квіти для авторських букетів, композицій та декорування інтер'єру.",
        icon_emoji="🌹"
    )
    cat_indoor = Category.objects.create(
        name="Кімнатні рослини",
        slug="indoor-plants",
        description="Горщикові декоративно-листяні та квітучі рослини для створення домашнього затишку.",
        icon_emoji="🪴"
    )
    cat_dried = Category.objects.create(
        name="Сухоцвіти та лаванда",
        slug="dried-flowers",
        description="Довговічні стабілізовані квіти, кримська лаванда та польові сухоцвіти, що не в'януть роками.",
        icon_emoji="🌾"
    )
    cat_exotic = Category.objects.create(
        name="Екзотичні квіти",
        slug="exotic-flowers",
        description="Рідкісні види орхідей, антуріуми, протеї та стреліції для особливих урочистих подій.",
        icon_emoji="🌺"
    )

    # 4. Створення приводів / подій (В3.1, Д1)
    occ_wedding = Occasion.objects.create(
        name="Весілля",
        slug="wedding",
        description="Ніжні, пастельні тони: півонії, троянди, еустоми для букета нареченої та оформлення зали.",
        season="all_year",
        badge_color="secondary"
    )
    occ_bday = Occasion.objects.create(
        name="День народження",
        slug="birthday",
        description="Яскраві, радісні композиції для щирих побажань гарного настрою.",
        season="all_year",
        badge_color="info"
    )
    occ_romance = Occasion.objects.create(
        name="Романтичне побачення",
        slug="romance",
        description="Класичні червоні та рожеві троянди, чуттєві аромати для вираження кохання.",
        season="all_year",
        badge_color="danger"
    )
    occ_mom = Occasion.objects.create(
        name="День матері",
        slug="mothers-day",
        description="Зворушливі весняні квіти, тюльпани та гортензії для найрідніших мам.",
        season="spring",
        badge_color="success"
    )
    occ_business = Occasion.objects.create(
        name="Діловий протокол",
        slug="business",
        description="Стримані, елегантні композиції у вертикальному стилі для колег і партнерів.",
        season="all_year",
        badge_color="dark"
    )

    # 5. Створення квітів (В3.1, В3.2, В3.5)
    f1 = Flower.objects.create(
        name="Півонія 'Сара Бернар'",
        latin_name="Paeonia lactiflora",
        category=cat_cut,
        description="Ніжно-рожева перлина флористики. Пишні махрові пелюстки з ніжним пудровим ароматом символізують процвітання, благополуччя та романтичне кохання.",
        price=180.00,
        in_stock=True,
        difficulty_level="medium",
        image_url="https://images.unsplash.com/photo-1563245372-f21724e3856d?auto=format&fit=crop&w=800&q=80",
        owner=florist_user
    )
    f1.occasions.add(occ_wedding, occ_romance, occ_mom)

    f2 = Flower.objects.create(
        name="Троянда чайно-гібридна 'Ред Наомі'",
        latin_name="Rosa hybrida",
        category=cat_cut,
        description="Королева класичного букета. Оксамитові пелюстки насиченого темно-рубінового кольору та витончений тонкий аромат. Має чудову стійкість у вазі.",
        price=95.00,
        in_stock=True,
        difficulty_level="easy",
        image_url="https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=800&q=80",
        owner=florist_user
    )
    f2.occasions.add(occ_romance, occ_bday, occ_business)

    f3 = Flower.objects.create(
        name="Гортензія крупнолиста 'Рожева Мрія'",
        latin_name="Hydrangea macrophylla",
        category=cat_cut,
        description="Об'ємні пишні суцвіття пастельного відтінку. Створює неперевершений об'єм та легкість у будь-якій квітковій композиції.",
        price=240.00,
        in_stock=True,
        difficulty_level="hard",
        image_url="https://images.unsplash.com/photo-1508615039623-a25605d2b022?auto=format&fit=crop&w=800&q=80",
        owner=florist_user
    )
    f3.occasions.add(occ_wedding, occ_bday, occ_mom)

    f4 = Flower.objects.create(
        name="Еустома великоквіткова (Лізіантус)",
        latin_name="Eustoma grandiflorum",
        category=cat_cut,
        description="Японська троянда із шовковистими хвилястими пелюстками кремово-рожевого відтінку. Надзвичайно ніжна, відкривається поступово протягом двох тижнів.",
        price=85.00,
        in_stock=True,
        difficulty_level="easy",
        image_url="https://images.unsplash.com/photo-1526047932273-341f2a7631f9?auto=format&fit=crop&w=800&q=80",
        owner=florist_user
    )
    f4.occasions.add(occ_wedding, occ_mom, occ_bday)

    f5 = Flower.objects.create(
        name="Орхідея Фаленопсис 'Білий Метелик'",
        latin_name="Phalaenopsis aphrodite",
        category=cat_indoor,
        description="Вишукана кімнатна орхідея з каскадом білосніжних квітів. Цвіте від двох до чотирьох місяців, очищує повітря та дарує естетичну гармонію.",
        price=490.00,
        in_stock=True,
        difficulty_level="medium",
        image_url="https://images.unsplash.com/photo-1525310072745-f49212b5ac6d?auto=format&fit=crop&w=800&q=80",
        owner=florist_user
    )
    f5.occasions.add(occ_bday, occ_business, occ_wedding)

    f6 = Flower.objects.create(
        name="Лаванда вузьколиста 'Прованс'",
        latin_name="Lavandula angustifolia",
        category=cat_dried,
        description="Ароматний букет сухоцвітів гірської лаванди. Має заспокійливий фітотерапевтичний ефект, зберігає фіолетовий колір і тонкий аромат роками.",
        price=150.00,
        in_stock=True,
        difficulty_level="easy",
        image_url="https://images.unsplash.com/photo-1500964757637-c85e8a162699?auto=format&fit=crop&w=800&q=80",
        owner=florist_user
    )
    f6.occasions.add(occ_romance, occ_mom)

    f7 = Flower.objects.create(
        name="Монстера делікатесна",
        latin_name="Monstera deliciosa",
        category=cat_indoor,
        description="Легендарна тропічна рослина з різьбленим глянцевим листям смарагдового кольору. Ідеальний вибір для сучасного скандинавського інтер'єру.",
        price=620.00,
        in_stock=False,
        difficulty_level="easy",
        image_url="https://images.unsplash.com/photo-1614594975525-e45190c55d0b?auto=format&fit=crop&w=800&q=80",
        owner=florist_user
    )
    f7.occasions.add(occ_business, occ_bday)

    f8 = Flower.objects.create(
        name="Стреліція королівська 'Райський Птах'",
        latin_name="Strelitzia reginae",
        category=cat_exotic,
        description="Екзотична квітка з Південної Африки, форма суцвіття якої нагадує чубок райського птаха. Яскраві помаранчево-блакитні барви вражають уяву.",
        price=320.00,
        in_stock=True,
        difficulty_level="hard",
        image_url="https://images.unsplash.com/photo-1551893478-d726eaf0442c?auto=format&fit=crop&w=800&q=80",
        owner=florist_user
    )
    f8.occasions.add(occ_business, occ_bday)

    # 6. Створення довідників з догляду (В3.1, В3.2, В3.5)
    CareGuide.objects.create(
        flower=f1,
        watering_frequency_days=1,
        temperature_range="16-19°C",
        light_requirement="bright_indirect",
        humidity_level="medium",
        stem_cutting_tips="Підрізати стебла під кутом 45 градусів гострим секатором або ножем під струменем води. Видалити все листя, що занурюється у воду.",
        florist_secret="Додайте у вазу половинку пакетика Chrysal або 1 чайну ложку цукру з кількома краплями лимонного соку для швидкого розкриття бутонів.",
        expert=florist_user
    )

    CareGuide.objects.create(
        flower=f2,
        watering_frequency_days=1,
        temperature_range="15-18°C",
        light_requirement="partial_shade",
        humidity_level="medium",
        stem_cutting_tips="Зрізати навскіс на 2-3 см кожні два дні. Занурювати у високу вазу з холодною водою мінімум на 50% висоти стебла.",
        florist_secret="Троянди не терплять сусідства з яблуками та бананами (етилен прискорює в'янення) та протягів від кондиціонера.",
        expert=florist_user
    )

    CareGuide.objects.create(
        flower=f3,
        watering_frequency_days=1,
        temperature_range="17-20°C",
        light_requirement="partial_shade",
        humidity_level="high",
        stem_cutting_tips="Зробити поздовжній надріз стебла на 1 см знизу. Гортензія надзвичайно вологолюбна — обприскуйте пелюстки м'якою водою.",
        florist_secret="Якщо суцвіття опустило пелюстки, повністю занурте шапку квітки у прохолодну воду на 30 хвилин — вона повністю оживе!",
        expert=florist_user
    )

    CareGuide.objects.create(
        flower=f4,
        watering_frequency_days=2,
        temperature_range="18-22°C",
        light_requirement="bright_indirect",
        humidity_level="medium",
        stem_cutting_tips="Стебла еустоми тонкі й тендітні, зрізайте над вузликом. Води у вазі має бути помірна кількість (близько 10 см).",
        florist_secret="Своєчасно видаляйте квіти, які вже відцвіли, щоб інші пуп'янки мали силу повністю розкритися.",
        expert=florist_user
    )

    CareGuide.objects.create(
        flower=f5,
        watering_frequency_days=7,
        temperature_range="20-25°C",
        light_requirement="bright_indirect",
        humidity_level="medium",
        stem_cutting_tips="Горщикова рослина: полив методом занурення горщика у відстояну воду кімнатної температури на 15-20 хвилин.",
        florist_secret="Коріння повинно отримувати світло, тому висаджуйте фаленопсис виключно у прозорий пластиковий горщик з кори.",
        expert=florist_user
    )

    CareGuide.objects.create(
        flower=f6,
        watering_frequency_days=0,
        temperature_range="15-25°C",
        light_requirement="shade",
        humidity_level="low",
        stem_cutting_tips="Сухоцвіт не потребує води взагалі! Тримайте вазу абсолютно сухою подалі від підвищеної вологості (не у ванній).",
        florist_secret="Для відновлення інтенсивності аромату через рік просто легенько розітріть пальцями кілька квіточок у букеті.",
        expert=florist_user
    )

    # 7. Додавання демонстраційного обраного (В3.1)
    Favorite.objects.create(user=client_user, flower=f1)
    Favorite.objects.create(user=client_user, flower=f4)


def reverse_seed_data(apps, schema_editor):
    Category = apps.get_model("catalog", "Category")
    Category.objects.all().delete()
    Occasion = apps.get_model("catalog", "Occasion")
    Occasion.objects.all().delete()
    Flower = apps.get_model("catalog", "Flower")
    Flower.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0001_initial"),
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.RunPython(seed_data, reverse_seed_data),
    ]
