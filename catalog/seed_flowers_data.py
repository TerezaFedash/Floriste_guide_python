# catalog/seed_flowers_data.py


FLOWERS_DATA = [

    {
        "name": "Троянда",
        "latin_name": "Rosa",
        "category_slug": "cut-flowers",
        "description": "Класична королева флористики з бездоганною формою бутона та витонченим шляхетним ароматом. Символізує глибоке кохання, захоплення та повагу. Є основою для найрозкішніших романтичних та весільних композицій.",
        "fun_fact": "Скам'янілим решткам найдавніших предків троянди понад 35 мільйонів років — вони квітли на Землі задовго до появи людини.",
        "difficulty_level": "medium",
        "image_url": "https://images.unsplash.com/photo-1581938165093-050aeb5ef218?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTh8fHJvc2VzfGVufDB8fDB8fHww&utm_source=chatgpt.com",
        "occasions": ["wedding", "romance", "birthday"],
        "care": {
            "watering_frequency_days": 1,
            "temperature_range": "16-19°C",
            "light_requirement": "bright_indirect",
            "humidity_level": "medium",
            "soil_type": "Чиста прохолодна відстояна вода без ґрунту",
            "stem_cutting_tips": "Підрізати стебло під кутом 45 градусів гострим ножем під струменем води. Видалити листя, що занурюється у воду.",
            "florist_secret": "Додайте у воду спеціальний флористичний кризал або кілька крапель лимонного соку для дезінфекції та живлення стебла.",
            "fun_fact": "Трояндова ефірна олія — одна з найдорожчих у парфумерії: для отримання одного кілограма олії потрібно близько трьох тонн пелюсток."
        }
    },
    {
        "name": "Тюльпан",
        "latin_name": "Tulipa",
        "category_slug": "cut-flowers",
        "description": "Свіжа та життєрадісна весняна квітка з витонченим келихоподібним бутоном і соковитою зеленню. Втілює оновлення, ніжність, гармонію та прихід весняного тепла.",
        "fun_fact": "У зрізаному вигляді тюльпани продовжують рости у вазі, витягуючись ще на кілька сантиметрів у напрямку до світла.",
        "difficulty_level": "easy",
        "image_url": "https://plus.unsplash.com/premium_photo-1676272769520-e0b5af99c509?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8dHVsaXB8ZW58MHx8MHx8fDA%3D&utm_source=chatgpt.com",
        "occasions": ["mothers-day", "birthday", "romance"],
        "care": {
            "watering_frequency_days": 1,
            "temperature_range": "14-17°C",
            "light_requirement": "bright_indirect",
            "humidity_level": "medium",
            "soil_type": "Крижана відстояна вода (рівень 3-5 см)",
            "stem_cutting_tips": "Наливати мінімальну кількість крижаної води (3-5 см). Зріз робити прямим, оновлюючи щодня.",
            "florist_secret": "Додавання кубиків льоду у вазу щоранку суттєво уповільнює розкриття бутонів і подовжує свіжість тюльпанів до 10-12 днів.",
            "fun_fact": "У Нідерландах XVII століття під час 'тюльпаноманії' одна цибулина рідкісного сорту могла коштувати стільки ж, скільки кам'яний будинок в Амстердамі."
        }
    },
    {
        "name": "Соняшник",
        "latin_name": "Helianthus annuus",
        "category_slug": "cut-flowers",
        "description": "Яскравий сонячний велетень з теплими золотавими пелюстками та оксамитовим темним кошиком. Символ життєвої енергії, оптимізму, миру, родючості та тепла.",
        "fun_fact": "Молоді суцвіття соняшника мають унікальну властивість геліотропізму — вони повертають свої голівки слідом за сонцем зі сходу на захід.",
        "difficulty_level": "easy",
        "image_url": "https://images.unsplash.com/photo-1512238701577-f182d9ef8af7?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTl8fHN1bmZsb3dlcnxlbnwwfHwwfHx8MA%3D%3D&utm_source=chatgpt.com",
        "occasions": ["birthday", "business"],
        "care": {
            "watering_frequency_days": 1,
            "temperature_range": "18-22°C",
            "light_requirement": "bright_indirect",
            "humidity_level": "low",
            "soil_type": "Глибока ваза зі свіжою водою",
            "stem_cutting_tips": "Стебла соняшника товсті та потребують глибокої води. Оновлюйте косий зріз щодня та знімайте нижнє листя.",
            "florist_secret": "Опустіть кінчики стебел на 15 секунд в окріп перед тим як поставити у холодну воду — це вижене повітряні пробки з капілярів.",
            "fun_fact": "Одне суцвіття соняшника насправді є кошиком, складеним із тисяч дрібних індивідуальних квіточок."
        }
    },
    {
        "name": "Хризантема",
        "latin_name": "Chrysanthemum",
        "category_slug": "cut-flowers",
        "description": "Осіння королева садів із дивовижною стійкістю та багатством форм — від голчастих до пишних помпонних. Символізує довголіття, радість, мудрість і вірність.",
        "fun_fact": "В Японії хризантема є священним символом імператорського дому та найвищої влади, а також емблемою на національному паспорті.",
        "difficulty_level": "easy",
        "image_url": "https://images.unsplash.com/photo-1554727434-e842126abc82?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTB8fGNocnlzYW50aGVtdW1zfGVufDB8fDB8fHww&utm_source=chatgpt.com",
        "occasions": ["birthday", "business", "mothers-day"],
        "care": {
            "watering_frequency_days": 2,
            "temperature_range": "15-20°C",
            "light_requirement": "bright_indirect",
            "humidity_level": "medium",
            "soil_type": "Свіжа чиста вода у вазі",
            "stem_cutting_tips": "Стебла хризантеми краще не різати металевими ножицями, а акуратно розщеплювати або обламувати знизу для кращого водопоглинання.",
            "florist_secret": "Хризантеми можуть стояти у вазі понад три тижні, якщо регулярно міняти воду та прибирати листя нижче водної лінії.",
            "fun_fact": "Назва квітки походить від грецьких слів 'chrysos' (золото) та 'anthemon' (квітка) — перші дикі хризантеми були виключно золотисто-жовтими."
        }
    },
    {
        "name": "Півонія",
        "latin_name": "Paeonia lactiflora",
        "category_slug": "cut-flowers",
        "description": "Пишна шовковиста перлина весняно-літнього сезону з неповторним запашним ароматом та сотнями ніжних хвилястих пелюсток. Символ щасливого шлюбу, багатства та романтики.",
        "fun_fact": "У Китаї півонія вважається національним надбанням і символом імператорського багатства вже понад півтори тисячі років.",
        "difficulty_level": "medium",
        "image_url": "https://images.unsplash.com/photo-1657008292833-3abab79e04dd?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8cGlvbnN8ZW58MHx8MHx8fDA%3D&utm_source=chatgpt.com",
        "occasions": ["wedding", "romance", "mothers-day"],
        "care": {
            "watering_frequency_days": 1,
            "temperature_range": "16-20°C",
            "light_requirement": "bright_indirect",
            "humidity_level": "medium",
            "soil_type": "Прохолодна свіжа вода",
            "stem_cutting_tips": "Підрізайте стебла під кутом 45 градусів. Якщо бутони занадто тугі, змийте теплуватою водою крапельки солодкого нектару з пелюсток.",
            "florist_secret": "Якщо потрібно прискорити розкриття бутона перед святом, поставте півонії у теплу воду в добре освітлену кімнату на 2-3 години.",
            "fun_fact": "Кущ деревоподібної півонії може жити та пишно цвісти понад сто років на одному місці."
        }
    },
    {
        "name": "Гербера",
        "latin_name": "Gerbera jamesonii",
        "category_slug": "cut-flowers",
        "description": "Життєрадісна південноафриканська ромашка яскравих соковитих відтінків. Її правильні графічні форми символізують таємничість, оптимізм, посмішку та відкритість світу.",
        "fun_fact": "Гербера посідає п'яте місце у світі за популярністю серед зрізаних квітів після троянди, гвоздики, хризантеми та тюльпана.",
        "difficulty_level": "easy",
        "image_url": "https://images.unsplash.com/photo-1597583995844-edce63cc1cb0?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Z2VyYmVyYXxlbnwwfHwwfHx8MA%3D%3D&utm_source=chatgpt.com",
        "occasions": ["birthday", "business"],
        "care": {
            "watering_frequency_days": 1,
            "temperature_range": "18-21°C",
            "light_requirement": "bright_indirect",
            "humidity_level": "medium",
            "soil_type": "Неглибока вода (4-5 см)",
            "stem_cutting_tips": "Гербера має опушене стебло, схильне до загнивання. Наливайте у вазу не більше 4-5 см води та підрізайте кінчик щодня.",
            "florist_secret": "Використовуйте флористичні трубочки або спеціальний дріт, щоб підтримувати важкі суцвіття у вертикальному положенні.",
            "fun_fact": "Гербера була названа на честь німецького лікаря і ботаніка Трауготта Гербера, який досліджував флору Східної Європи."
        }
    },
    {
        "name": "Гіацинт",
        "latin_name": "Hyacinthus orientalis",
        "category_slug": "cut-flowers",
        "description": "Пишне щільне суцвіття із десятків мініатюрних дзвіночків з насиченим солодко-медовим весняним ароматом. Символізує відродження природи, вірність та радість зустрічі.",
        "fun_fact": "У давньогрецькому міфі гіацинт виріс із крові прекрасного юнака Гіацинта, улюбленця бога сонця Аполлона.",
        "difficulty_level": "easy",
        "image_url": "https://media.istockphoto.com/id/471792331/photo/multicolored-hyacinths.webp?a=1&b=1&s=612x612&w=0&k=20&c=LEdikxUNECAjgtgFq7an2osUgD8dtGYcge8k4gl8dRI=&utm_source=chatgpt.com",
        "occasions": ["mothers-day", "birthday"],
        "care": {
            "watering_frequency_days": 2,
            "temperature_range": "14-18°C",
            "light_requirement": "bright_indirect",
            "humidity_level": "medium",
            "soil_type": "Холодна чиста вода (4-6 см)",
            "stem_cutting_tips": "Не зрізайте денце цибулини, якщо гіацинт продається з нею — з денцем квітка простоїть у вазі майже вдвічі довше.",
            "florist_secret": "Гіацинти виділяють слиз, тому перед додаванням до збірного букета потримайте їх окремо у воді кілька годин.",
            "fun_fact": "Один гіацинт здатний наповнити ніжним ароматом цілу простору кімнату без будь-яких додаткових ароматизаторів."
        }
    },
    {
        "name": "Нарцис",
        "latin_name": "Narcissus",
        "category_slug": "cut-flowers",
        "description": "Сяюча сонячна весняна квітка з виразною коронкою та контрастними пелюстками. Означає благородство, самоповагу, оновлення почуттів та весняну надію.",
        "fun_fact": "Нарциси є символом Уельсу, де їхнє цвітіння збігається з національним святом — Днем святого Давида.",
        "difficulty_level": "easy",
        "image_url": "https://images.unsplash.com/photo-1614888773556-4bf9ab1a8675?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8bmFyY2lzc3VzfGVufDB8fDB8fHww&utm_source=chatgpt.com",
        "occasions": ["mothers-day", "birthday"],
        "care": {
            "watering_frequency_days": 1,
            "temperature_range": "15-18°C",
            "light_requirement": "bright_indirect",
            "humidity_level": "medium",
            "soil_type": "Прохолодна вода (3-5 см)",
            "stem_cutting_tips": "Нарциси виділяють густий сік після зрізання, шкідливий для інших квітів. Поставте їх на добу в окрему вазу перед комбінуванням.",
            "florist_secret": "Ніколи не підрізайте нарциси повторно після того, як вони вже постояли у воді та сік перестав виділятися.",
            "fun_fact": "Назва квітки походить від грецького слова 'narke' (заціпеніння або дурман) через її солодкий пряний запах."
        }
    },
    {
        "name": "Лілія",
        "latin_name": "Lilium",
        "category_slug": "cut-flowers",
        "description": "Велична аристократична квітка з витонченими восковими пелюстками та неповторним царським силуетом. Уособлює чистоту, велич, духовне благородство та розкіш.",
        "fun_fact": "Геральдична лілія (fleur-de-lis) протягом століть була головним державним символом французької королівської династії.",
        "difficulty_level": "medium",
        "image_url": "https://images.unsplash.com/photo-1561897519-6e4fbd1fbc41?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8bGlsaXVtfGVufDB8fDB8fHww&utm_source=chatgpt.com",
        "occasions": ["wedding", "birthday", "business"],
        "care": {
            "watering_frequency_days": 2,
            "temperature_range": "17-21°C",
            "light_requirement": "bright_indirect",
            "humidity_level": "medium",
            "soil_type": "Глибока ваза з чистою водою",
            "stem_cutting_tips": "Своєчасно видаляйте пиляки з розкритих тичинок, щоб пилок не осипався та не фарбував пелюстки чи одяг.",
            "florist_secret": "Коли нижні бутони відцвітають, акуратно відщипуйте їх — це дозволить верхнім бутонам повноцінно розкритися.",
            "fun_fact": "Аромат східних гібридів лілій настільки інтенсивний, що не рекомендується залишати великі букети на ніч у спальні."
        }
    },
    {
        "name": "Ірис",
        "latin_name": "Iris germanica",
        "category_slug": "cut-flowers",
        "description": "Шляхетна квітка з химерною будовою суцвіття, що нагадує пурхання тропічного метелика. Символізує мудрість, віру, надію, хоробрість і добрі звістки.",
        "fun_fact": "Квітка отримала свою назву на честь Іриди — давньогрецької богині веселки, яка спускалася з неба, щоб передати волю богів людям.",
        "difficulty_level": "easy",
        "image_url": "https://images.unsplash.com/photo-1589312397744-799d9f9c2944?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8SXJpc3xlbnwwfHwwfHx8MA%3D%3D&utm_source=chatgpt.com",
        "occasions": ["birthday", "business"],
        "care": {
            "watering_frequency_days": 1,
            "temperature_range": "15-19°C",
            "light_requirement": "bright_indirect",
            "humidity_level": "medium",
            "soil_type": "Прохолодна вода (5-7 см)",
            "stem_cutting_tips": "Іриси дуже люблять прохолоду. Міняйте воду щодня, освіжаючи прямий зріз стебла на 1 см.",
            "florist_secret": "Додавання шматочка деревного вугілля у вазу запобігає розмноженню бактерій та подовжує цвітіння розкритих стрілок.",
            "fun_fact": "З кореневищ ірису виготовляють легендарний 'ірисовий корінь' (орріс) — один із найцінніших фіксаторів у селективній парфумерії."
        }
    },
    {
        "name": "Фрезія",
        "latin_name": "Freesia refracta",
        "category_slug": "cut-flowers",
        "description": "Аристократична витончена квітка з ніжними дзвіночками, що вишикувалися на вигнутому квітконосі. Володіє легким свіжим ароматом з цитрусовими нотками.",
        "fun_fact": "У вікторіанській мові квітів фрезія вважалася абсолютним символом беззастережної довіри та міцної дружби.",
        "difficulty_level": "easy",
        "image_url": "https://images.unsplash.com/photo-1712309566108-85422f2466ff?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8RnJlZXNpYXxlbnwwfHwwfHx8MA%3D%3D&utm_source=chatgpt.com",
        "occasions": ["wedding", "romance", "mothers-day"],
        "care": {
            "watering_frequency_days": 1,
            "temperature_range": "16-19°C",
            "light_requirement": "bright_indirect",
            "humidity_level": "medium",
            "soil_type": "Свіжа чиста відстояна вода",
            "stem_cutting_tips": "Підрізайте стебла під кутом гострим ножем і ставте у вазу з 5-7 см свіжої прохолодної води.",
            "florist_secret": "Видаляйте перші зів'ялі дзвіночки на початку гілочки, щоб дати енергію для розкриття кінцевим мініатюрним бутонам.",
            "fun_fact": "Фрезія настільки чутлива до чистоти води, що погано переносить хлоровану воду — дайте воді відстоятися не менше доби."
        }
    },
    {
        "name": "Гортензія",
        "latin_name": "Hydrangea macrophylla",
        "category_slug": "cut-flowers",
        "description": "Велична об'ємна квітка-хмаринка з десятків тонких пелюсток ніжних пастельних відтінків. Втілює щирість почуттів, безмежну вдячність, доброту та легкість.",
        "fun_fact": "Забарвлення пелюсток гортензії залежить від кислотності ґрунту: на кислих ґрунтах вона блакитна, а на лужних — рожева.",
        "difficulty_level": "hard",
        "image_url": "https://images.unsplash.com/photo-1501577316686-a5cbf6c1df7e?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8aHlkcmFuZ2VhfGVufDB8fDB8fHww&utm_source=chatgpt.com",
        "occasions": ["wedding", "mothers-day", "birthday"],
        "care": {
            "watering_frequency_days": 1,
            "temperature_range": "15-18°C",
            "light_requirement": "bright_indirect",
            "humidity_level": "high",
            "soil_type": "Глибока прохолодна вода (до 2/3 вази)",
            "stem_cutting_tips": "Стебло тверде та дерев'янисте: зріжте під кутом і зробіть вертикальний надріз вздовж стебла на 2-3 см для максимального поглинання води.",
            "florist_secret": "Якщо шапка гортензії прив'яла, занурте всю квітку разом із суцвіттям у ванночку з прохолодною водою на 20-30 хвилин — вона повністю оживе.",
            "fun_fact": "Ботанічна назва Hydrangea походить від грецьких слів 'hydor' (вода) та 'angeion' (посудина), що підкреслює її неймовірну спрагу до вологи."
        }
    },
    {
        "name": "Ромашка",
        "latin_name": "Matricaria chamomilla",
        "category_slug": "cut-flowers",
        "description": "Зворушлива і щира квітка літнього сонця з білими шовковистими промінцями та теплою золотою серцевиною. Символ чистоти, юності, романтичних мрій та домашнього затишку.",
        "fun_fact": "Ромашка здавна використовується в народній медицині завдяки антисептичним властивостям її ефірної олії хамазулену.",
        "difficulty_level": "easy",
        "image_url": "https://media.istockphoto.com/id/2218584936/photo/chamomile-flowers-growing.webp?a=1&b=1&s=612x612&w=0&k=20&c=fb0lCY0MCcdUV8R0jtchW3LwdSby3q2RSAaozexXpWM=&utm_source=chatgpt.com",
        "occasions": ["birthday", "romance", "mothers-day"],
        "care": {
            "watering_frequency_days": 1,
            "temperature_range": "17-21°C",
            "light_requirement": "bright_indirect",
            "humidity_level": "low",
            "soil_type": "Чиста вода у вазі",
            "stem_cutting_tips": "Регулярно видаляйте нижні листочки, які торкаються води, щоб запобігти її замутненню.",
            "florist_secret": "Щодня оновлюйте зріз стебла на кілька міліметрів під струменем води для збереження пружності суцвіть.",
            "fun_fact": "Назва 'ромашка' виникла від латинського слова 'romana' (римська), коли в середньовічні травники рослину завезли як 'римську траву'."
        }
    },
    {
        "name": "Ранункулюс",
        "latin_name": "Ranunculus asiaticus",
        "category_slug": "cut-flowers",
        "description": "Азіатський жовтець надзвичайної краси з сотнями тонких воскових пелюсток, складених у щільний геометрично досконалий бутон. Символізує чарівність, шарм і привабливість.",
        "fun_fact": "Незважаючи на розкішний садовий вигляд, ранункулюс є близьким родичем дикого польового жовтця.",
        "difficulty_level": "medium",
        "image_url": "https://media.istockphoto.com/id/530190306/ru/%D1%84%D0%BE%D1%82%D0%BE/%D0%B1%D1%83%D0%BA%D0%B5%D1%82-%D0%B8%D0%B7-%D0%B1%D0%BB%D0%B5%D0%B4%D0%BD%D0%BE-%D1%80%D0%BE%D0%B7%D0%BE%D0%B2%D1%8B%D0%B9-%D1%80%D0%B0%D0%BD%D1%83%D0%BD%D0%BA%D1%83%D0%BB%D1%8E%D1%81-%D0%BF%D0%B5%D1%80%D1%81%D0%B8%D0%B4%D1%81%D0%BA%D0%B8%D0%B9-%D0%BB%D1%8E%D1%82%D0%B8%D0%BA-%D1%81%D0%B2%D0%B5%D1%82-%D1%84%D0%BE%D0%BD-%D0%B4%D0%B5%D1%80%D0%B5%D0%B2%D1%8F%D0%BD%D0%BD%D0%BE%D0%B9.jpg?s=612x612&w=0&k=20&c=LwH7qPxIAeEYRbOte9TGAKONEcnqtOS573B8fW2m494=&utm_source=chatgpt.com",
        "occasions": ["wedding", "romance", "birthday"],
        "care": {
            "watering_frequency_days": 2,
            "temperature_range": "15-18°C",
            "light_requirement": "bright_indirect",
            "humidity_level": "medium",
            "soil_type": "Помірна кількість чистої води (5-8 см)",
            "stem_cutting_tips": "Стебло порожнисте та ніжне, тому не наливайте занадто багато води у вазу, щоб уникнути загнивання основи.",
            "florist_secret": "Тримайте букет подалі від прямого сонячного світла та джерел тепла — у прохолоді ранункулюс стоїть до двох тижнів.",
            "fun_fact": "Латинська назва Ranunculus перекладається як 'маленька жабка', оскільки багато диких видів цієї рослини ростуть у вологих низинах біля водойм."
        }
    },
    {
        "name": "Еустома",
        "latin_name": "Eustoma grandiflorum",
        "category_slug": "cut-flowers",
        "description": "Витончена 'ірландська троянда' з ніжними шовковистими пелюстками та великою кількістю бутонів на кожній гілочці. Уособлює радість, грацію, ніжність і тривале кохання.",
        "fun_fact": "У зрізі еустома здатна розкривати навіть найменші зелені бутончики протягом двох-трьох тижнів поспіль.",
        "difficulty_level": "easy",
        "image_url": "https://media.istockphoto.com/id/2240326107/ru/%D1%84%D0%BE%D1%82%D0%BE/%D0%B1%D1%83%D0%BA%D0%B5%D1%82-%D0%B8%D0%B7-%D0%BF%D1%80%D0%B5%D0%BA%D1%80%D0%B0%D1%81%D0%BD%D1%8B%D1%85-%D1%80%D0%BE%D0%B7%D0%BE%D0%B2%D1%8B%D1%85-%D1%86%D0%B2%D0%B5%D1%82%D0%BE%D0%B2-%D1%8D%D1%83%D1%81%D1%82%D0%BE%D0%BC%D1%8B.jpg?s=612x612&w=0&k=20&c=n0sppXt4IjPFPUC5xZPXsQJbdwVF_H9wJo7S41zaZT0=&utm_source=chatgpt.com",
        "occasions": ["wedding", "mothers-day", "birthday"],
        "care": {
            "watering_frequency_days": 2,
            "temperature_range": "17-21°C",
            "light_requirement": "bright_indirect",
            "humidity_level": "medium",
            "soil_type": "Свіжа чиста вода у вазі",
            "stem_cutting_tips": "Зрізайте стебла під кутом між вузлами та своєчасно прибирайте квіти, що вже завершили цвітіння.",
            "florist_secret": "Еустома одна з найстійкіших зрізаних квітів: регулярна зміна води та підрізання гарантують свіжість букета понад 15-18 днів.",
            "fun_fact": "У дикій природі еустома росте у вологих преріях Північної Америки, де її називають 'дзвіночком прерій'."
        }
    },

   
    {
        "name": "Орхідея",
        "latin_name": "Phalaenopsis",
        "category_slug": "indoor-plants",
        "description": "Елегантна кімнатна квітка-метелик з тривалим періодом пишного цвітіння на дугоподібних квітконосах. Символізує гармонію, витонченість, затишок та досконалість.",
        "fun_fact": "У природі орхідеї-фаленопсиси є епіфітами: вони ростуть на корі дерев у тропічних лісах, вбираючи вологу корінням просто з повітря.",
        "difficulty_level": "medium",
        "image_url": "https://images.unsplash.com/photo-1454262041357-5d96f50a2f27?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTB8fG9yY2hpZCUyMGZsb3dlcnxlbnwwfHwwfHx8MA%3D%3D&utm_source=chatgpt.com",
        "occasions": ["birthday", "mothers-day", "business"],
        "care": {
            "watering_frequency_days": 7,
            "temperature_range": "18-24°C",
            "light_requirement": "bright_indirect",
            "humidity_level": "medium",
            "soil_type": "Спеціальний субстрат із соснової кори та моху сфагнуму",
            "stem_cutting_tips": "Поливати методом занурення горщика у відстояну воду на 15-20 хвилин раз на тиждень, коли коріння набуває сріблястого відтінку.",
            "florist_secret": "Орхідеям потрібен прозорий пластиковий горщик, оскільки їхнє коріння бере активну участь у фотосинтезі разом із листям.",
            "fun_fact": "Квіти фаленопсиса можуть триматися на квітконосі свіжими до чотирьох місяців поспіль."
        }
    },
    {
        "name": "Фіалка",
        "latin_name": "Saintpaulia",
        "category_slug": "indoor-plants",
        "description": "Улюблена мініатюрна кімнатна рослина з оксамитовим круглим листям та яскравими квіточками найрізноманітніших відтінків. Дарує оселі тепло, спокій і добробут.",
        "fun_fact": "Сенполія була вперше виявлена німецьким бароном Вальтером фон Сен-Полем у горах Східної Африки наприкінці XIX століття.",
        "difficulty_level": "easy",
        "image_url": "https://images.unsplash.com/photo-1777250735196-6244716588e8?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTR8fFNhaW50cGF1bGlhfGVufDB8fDB8fHww&utm_source=chatgpt.com",
        "occasions": ["mothers-day", "birthday"],
        "care": {
            "watering_frequency_days": 4,
            "temperature_range": "18-22°C",
            "light_requirement": "bright_indirect",
            "humidity_level": "medium",
            "soil_type": "Легкий пухкий торф'яний ґрунт з перлітом",
            "stem_cutting_tips": "Поливати виключно в піддон або під корінь теплою водою, уникаючи потрапляння крапель на опушене листя.",
            "florist_secret": "Для безперервного цвітіння забезпечте фіалці світловий день тривалістю 12-14 годин без прямого пекучого сонця.",
            "fun_fact": "Фіалку можна легко розмножити в домашніх умовах лише одним здоровим зрізаним листочком, укоріненим у воді."
        }
    },
    {
        "name": "Алое вера",
        "latin_name": "Aloe vera",
        "category_slug": "indoor-plants",
        "description": "Легендарний сукулент з м'ясистим зубчастим листям, наповненим цілющим желеподібним соком. Символ довголіття, захисту дому, сили духу та міцного здоров'я.",
        "fun_fact": "Гель з листя алое містить понад 75 корисних речовин, вітамінів і мікроелементів, які прискорюють регенерацію шкіри.",
        "difficulty_level": "easy",
        "image_url": "https://images.unsplash.com/photo-1649264722111-5cff15f9d830?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8YWxvZXxlbnwwfHwwfHx8MA%3D%3D&utm_source=chatgpt.com",
        "occasions": ["business", "birthday"],
        "care": {
            "watering_frequency_days": 14,
            "temperature_range": "18-26°C",
            "light_requirement": "direct_sun",
            "humidity_level": "low",
            "soil_type": "Піщаний субстрат для сукулентів та кактусів з дренажем",
            "stem_cutting_tips": "Поливайте тільки після повного просихання земляної грудки. Взимку полив скорочують до одного разу на місяць.",
            "florist_secret": "Краще недолити алое, ніж перелити: застій вологи у коренях — єдина серйозна небезпека для цієї стійкої рослини.",
            "fun_fact": "Стародавні єгиптяни називали алое 'рослиною безсмертя' та зображували її на стінах гробниць фараонів."
        }
    },
    {
        "name": "Монстера",
        "latin_name": "Monstera deliciosa",
        "category_slug": "indoor-plants",
        "description": "Популярна тропічна ліана з великим блискучим листям виразної розрізної форми. Надає інтер'єру сучасної урбаністичної естетики та відчуття справжніх джунглів.",
        "fun_fact": "Назва рослини походить від латинського 'monstrosus' (дивовижний, незвичайний) через гігантські розміри її листя в природі.",
        "difficulty_level": "easy",
        "image_url": "https://plus.unsplash.com/premium_photo-1663962158789-0ab624c4f17d?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8TW9uc3RlcmF8ZW58MHx8MHx8fDA%3D&utm_source=chatgpt.com",
        "occasions": ["business", "birthday"],
        "care": {
            "watering_frequency_days": 6,
            "temperature_range": "19-24°C",
            "light_requirement": "bright_indirect",
            "humidity_level": "high",
            "soil_type": "Поживний повітропроникний ґрунт з корою та кокосовим волокном",
            "stem_cutting_tips": "Поливайте помірно після підсихання верхнього шару на 3-4 см. Періодично протирайте листя від пилу м'якою вологою серветкою.",
            "florist_secret": "Ніколи не зрізайте повітряне коріння монстери — спрямовуйте його назад у горщик до землі або на вологу опору з моху.",
            "fun_fact": "Отвори та розрізи на листі монстери еволюційно виникли для того, щоб тропічні зливи та вітер вільно проходили крізь лист, не ламаючи його."
        }
    },
    {
        "name": "Заміокулькас",
        "latin_name": "Zamioculcas zamiifolia",
        "category_slug": "indoor-plants",
        "description": "Стильний невибагливий 'доларовий вазон' з глянцевим темно-смарагдовим листям на товстих черешках. Символ фінансового процвітання, стабільності та ділового успіху.",
        "fun_fact": "Заміокулькас має великі підземні бульби, які накопичують запаси води на багато місяців посухи.",
        "difficulty_level": "easy",
        "image_url": "https://images.unsplash.com/photo-1632207691143-643e2a9a9361?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8emFtaW9jdWxjYXN8ZW58MHx8MHx8fDA%3D&utm_source=chatgpt.com",
        "occasions": ["business", "birthday"],
        "care": {
            "watering_frequency_days": 12,
            "temperature_range": "18-25°C",
            "light_requirement": "partial_shade",
            "humidity_level": "low",
            "soil_type": "Легкий субстрат з високим вмістом піску та перліту",
            "stem_cutting_tips": "Полив рідкісний: дайте ґрунту майже повністю просохнути між поливами. Взимку поливайте не частіше ніж раз на 3 тижні.",
            "florist_secret": "Заміокулькас чудово переносить тінисті офісні приміщення та штучне освітлення, залишаючись яскраво-зеленим.",
            "fun_fact": "Незважаючи на африканське походження, світову популярність рослина здобула лише після 1996 року завдяки голландським розплідникам."
        }
    },
    {
        "name": "Спатіфілум",
        "latin_name": "Spathiphyllum",
        "category_slug": "indoor-plants",
        "description": "Елегантна рослина, відома в народі як 'жіноче щастя', з глянцевим зеленим листям та білосніжними квітами-вітрилами. Символ миру, сімейного затишку та любові.",
        "fun_fact": "Спатіфілум визнано одним із найкращих природних фільтрів NASA для очищення повітря від токсичних часток бензолу та формальдегіду.",
        "difficulty_level": "easy",
        "image_url": "https://plus.unsplash.com/premium_photo-1708769592969-9f42825496a7?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8U3BhdGhpcGh5bGx1bXxlbnwwfHwwfHx8MA%3D%3D&utm_source=chatgpt.com",
        "occasions": ["mothers-day", "birthday", "business"],
        "care": {
            "watering_frequency_days": 4,
            "temperature_range": "18-23°C",
            "light_requirement": "bright_indirect",
            "humidity_level": "high",
            "soil_type": "Пухка суміш листової землі, торфу та піску",
            "stem_cutting_tips": "Підтримуйте постійну вологість без застою води в піддоні. Рослина сама показує спрагу, злегка опускаючи листочки.",
            "florist_secret": "Регулярне обприскування листя теплою водою сприяє активному закладанню нових квітконосів-вітрил.",
            "fun_fact": "Біле покривало спатіфілума насправді є видозміненим листком, який захищає справжнє суцвіття-качанчик."
        }
    },
    {
        "name": "Каланхое",
        "latin_name": "Kalanchoe blossfeldiana",
        "category_slug": "indoor-plants",
        "description": "Компактний квітучий сукулент з м'ясистим листям та яскравими шапками мініатюрних махрових квіточок. Символізує теплоту, турботу та невичерпну радість.",
        "fun_fact": "Каланхое було однією з перших квітучих рослин, відправлених у космос на орбітальну станцію 'Салют' для вивчення в умовах невагомості.",
        "difficulty_level": "easy",
        "image_url": "https://images.unsplash.com/photo-1629984927380-94d440fba762?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8S2FsYW5jaG9lJTIwYmxvc3NmZWxkaWFuYXxlbnwwfHwwfHx8MA%3D%3D&utm_source=chatgpt.com",
        "occasions": ["birthday", "mothers-day"],
        "care": {
            "watering_frequency_days": 7,
            "temperature_range": "17-23°C",
            "light_requirement": "bright_indirect",
            "humidity_level": "low",
            "soil_type": "Поживний дренований субстрат для сукулентів",
            "stem_cutting_tips": "Поливайте тільки тоді, коли верхній шар ґрунту повністю висохне. Уникайте потрапляння води в центр розетки.",
            "florist_secret": "Каланхое є рослиною короткого світлового дня: щоб воно знову зацвіло, протягом місяця обмежуйте освітлення до 9 годин на добу.",
            "fun_fact": "Сік каланхое має природні бактерицидні та ранозагоювальні властивості, тому його часто називають 'домашнім лікарем'."
        }
    },
    {
        "name": "Антуріум",
        "latin_name": "Anthurium andraeanum",
        "category_slug": "indoor-plants",
        "description": "Ефектна тропічна рослина з глянцевими червоними серцеподібними приквітками та золотистим суцвіттям, відома як 'чоловіче щастя'. Символ пристрасті, мужності та лідерства.",
        "fun_fact": "Яскраве глянцеве червоне серце антуріума — це приквіткове покривало, а не пелюстка квітки.",
        "difficulty_level": "medium",
        "image_url": "https://images.unsplash.com/photo-1594076353236-85d8e500be80?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8QW50aHVyaXVtJTIwYW5kcmFlYW51bXxlbnwwfHwwfHx8MA%3D%3D&utm_source=chatgpt.com",
        "occasions": ["business", "birthday", "romance"],
        "care": {
            "watering_frequency_days": 5,
            "temperature_range": "20-25°C",
            "light_requirement": "bright_indirect",
            "humidity_level": "high",
            "soil_type": "Кислий повітропроникний субстрат з корою, торфом і перлітом",
            "stem_cutting_tips": "Полив регулярний м'якою теплою водою без надлишку вологи в піддоні. Оберігайте від холодних протягів.",
            "florist_secret": "Листя антуріума любить вологу, але саме суцвіття-покривало обприскувати не варто, щоб на ньому не з'являлися плями.",
            "fun_fact": "Назва квітки походить від грецьких слів 'anthos' (квітка) і 'oura' (хвіст), описуючи форму суцвіття."
        }
    },
    {
        "name": "Драцена",
        "latin_name": "Dracaena marginata",
        "category_slug": "indoor-plants",
        "description": "Струнке інтер'єрне деревце з витонченим стовбуром та розкішною кроною з вузького листя з червоною облямівкою. Символізує внутрішню гармонію, стійкість та мир.",
        "fun_fact": "Назва рослини перекладається як 'самка дракона', оскільки смола деяких видів драцени має густий криваво-червоний колір.",
        "difficulty_level": "easy",
        "image_url": "https://images.unsplash.com/photo-1771654249968-cad93a1641e8?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8RHJhY2VuYSUyMG1hcmdpbmF0YXxlbnwwfHwwfHx8MA%3D%3D&utm_source=chatgpt.com",
        "occasions": ["business", "birthday"],
        "care": {
            "watering_frequency_days": 7,
            "temperature_range": "19-24°C",
            "light_requirement": "bright_indirect",
            "humidity_level": "medium",
            "soil_type": "Універсальний ґрунт з обов'язковим шаром керамзитового дренажу",
            "stem_cutting_tips": "Поливайте помірно після підсихання земляної грудки на глибину 2-3 см. Регулярно обприскуйте крону теплою водою.",
            "florist_secret": "Драцена дуже чутлива до вмісту фтору у воді: використовуйте фільтровану або добре відстояну воду кімнатної температури.",
            "fun_fact": "Драцена чудово зволожує сухе повітря у приміщенні з кондиціонерами чи центральним опаленням."
        }
    },
    {
        "name": "Грошове дерево",
        "latin_name": "Crassula ovata",
        "category_slug": "indoor-plants",
        "description": "Популярна кімнатна товстянка з товстим дерев'янистим стовбуром і округлим смарагдовим листям, схожим на монети. Символ достатку, накопичення енергії та фінансового успіху.",
        "fun_fact": "За правильного догляду та великої кількості сонячного світла товстянка взимку може цвісти ніжними біло-рожевими зірчастими квіточками.",
        "difficulty_level": "easy",
        "image_url": "https://images.unsplash.com/photo-1781409300371-79e15de878ae?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D",
        "occasions": ["business", "birthday"],
        "care": {
            "watering_frequency_days": 10,
            "temperature_range": "18-25°C",
            "light_requirement": "direct_sun",
            "humidity_level": "low",
            "soil_type": "Піщаний субстрат для кактусів та сукулентів",
            "stem_cutting_tips": "Полив рідкісний: листя накопичує воду, тому перелив для товстянки згубний. Забезпечте максимальну кількість сонячного світла.",
            "florist_secret": "Посадіть рослину у важкий глиняний горщик, щоб масивна крона не перекинула легку місткість під час росту.",
            "fun_fact": "Згідно з філософією фен-шуй, грошове дерево найкраще розташовувати у південно-східному секторі кімнати."
        }
    },
    {
        "name": "Фікус",
        "latin_name": "Ficus elastica",
        "category_slug": "indoor-plants",
        "description": "Шляхетний каучуконосний фікус з великим восковим листям глибокого смарагдового кольору. Створює відчуття монументальності, спокою, впевненості та захищеності.",
        "fun_fact": "У XIX столітті білий молочний сік цієї рослини використовували для експериментів з виробництва натурального каучуку.",
        "difficulty_level": "easy",
        "image_url": "https://images.unsplash.com/photo-1692275382147-4bf274cb77c1?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D",
        "occasions": ["business", "birthday"],
        "care": {
            "watering_frequency_days": 6,
            "temperature_range": "18-24°C",
            "light_requirement": "bright_indirect",
            "humidity_level": "medium",
            "soil_type": "Поживний гумусний ґрунт з торфом і розпушувачами",
            "stem_cutting_tips": "Поливайте помірно теплою водою, коли просохне верхній шар на 2 см. Бережіть від різких перепадів температур.",
            "florist_secret": "Для збереження дзеркального глянцю протирайте листя сумішшю води та невеликої кількості молока або м'якою губкою.",
            "fun_fact": "Фікус ефективно поглинає з повітря шкідливі випаровування побутової хімії та пластику."
        }
    },
    {
        "name": "Бегонія",
        "latin_name": "Begonia",
        "category_slug": "indoor-plants",
        "description": "Чарівна кімнатна рослина з асиметричним візерунчастим листям та яскравим каскадом барвистих квітів. Уособлює індивідуальність, гостинність, душевне тепло та творчість.",
        "fun_fact": "Рід бегоній був названий на честь Мішеля Бегона, французького губернатора Гаїті та пристрасного покровителя ботанічних експедицій XVII століття.",
        "difficulty_level": "medium",
        "image_url": "https://images.unsplash.com/photo-1629984957815-d5476f9a9146?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D",
        "occasions": ["mothers-day", "birthday"],
        "care": {
            "watering_frequency_days": 4,
            "temperature_range": "18-22°C",
            "light_requirement": "bright_indirect",
            "humidity_level": "medium",
            "soil_type": "Легкий пухкий слабкокислий ґрунт з вермикулітом",
            "stem_cutting_tips": "Поливайте регулярно після легкого підсихання поверхні, не допускаючи застою води. Уникайте прямого обприскування листя.",
            "florist_secret": "Бегонія полюбляє вологе повітря: замість обприскування поставте горщик на піддон з вологою галькою.",
            "fun_fact": "Бегонія нараховує понад дві тисячі диких видів і десятки тисяч гібридних сортів у світовій культурі."
        }
    },
    {
        "name": "Герань",
        "latin_name": "Pelargonium",
        "category_slug": "indoor-plants",
        "description": "Традиційна домашня улюблениця з круглим пряно-ароматним листям і яскравими шапками квітів. Символізує домашній затишок, щиру дружбу, здоров'я та позитивну атмосферу.",
        "fun_fact": "Листя пеларгонії містить велику кількість фітонцидів, які очищують повітря в кімнаті та відлякують небажаних комах.",
        "difficulty_level": "easy",
        "image_url": "https://images.unsplash.com/photo-1567538737566-184fdf777891?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D",
        "occasions": ["mothers-day", "birthday"],
        "care": {
            "watering_frequency_days": 4,
            "temperature_range": "17-24°C",
            "light_requirement": "direct_sun",
            "humidity_level": "low",
            "soil_type": "Поживний дренований ґрунт з додаванням садової землі",
            "stem_cutting_tips": "Герань обожнює сонячні південні підвіконня. Поливайте помірно, коли просохне верхній шар землі.",
            "florist_secret": "Регулярна весняна обрізка та прищипування верхівок пагонів стимулюють утворення нових суцвіть і формують пишний кущ.",
            "fun_fact": "Ефірна олія герані за своїм хімічним складом та ароматом є популярною альтернативою дорогій трояндовій олії в парфумерії."
        }
    },
    {
        "name": "Бальзамін",
        "latin_name": "Impatiens walleriana",
        "category_slug": "indoor-plants",
        "description": "Життєрадісний 'вогник' або 'недоторка' з соковитими напівпрозорими пагонами та безперервним рясним цвітінням. Символ радості життя, привітності та щирості.",
        "fun_fact": "Назва 'Impatiens' (нетерплячий) пов'язана з тим, що дозрілий насіннєвий стручок при найменшому дотику миттєво 'вибухає', вистрілюючи насіння.",
        "difficulty_level": "easy",
        "image_url": "https://images.unsplash.com/photo-1652360474021-26d8aa68d7c1?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D",
        "occasions": ["mothers-day", "birthday"],
        "care": {
            "watering_frequency_days": 3,
            "temperature_range": "18-22°C",
            "light_requirement": "bright_indirect",
            "humidity_level": "medium",
            "soil_type": "Легкий вологоємний субстрат з торфом",
            "stem_cutting_tips": "Потребує регулярного та щедрого поливу, оскільки соковиті стебла швидко втрачають пружність при пересушуванні ґрунту.",
            "florist_secret": "У спекотні літні дні бальзамін вдячно реагує на вечірній теплий душ або м'яке обприскування.",
            "fun_fact": "Бальзамін здатен цвісти на підвіконні практично без перерви протягом усіх 12 місяців року."
        }
    },
    {
        "name": "Цикламен",
        "latin_name": "Cyclamen persicum",
        "category_slug": "indoor-plants",
        "description": "Вишукана зимовоквітуча рослина з мармуровим серцеподібним листям та вивернутими граційними пелюстками-метеликами. Символізує щирість, скромність і ніжні почуття.",
        "fun_fact": "Цикламен розквітає саме пізньої осені та взимку, коли більшість інших кімнатних рослин перебувають у стані спокою.",
        "difficulty_level": "medium",
        "image_url": "https://images.unsplash.com/photo-1654148818166-92db3dd2450d?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D",
        "occasions": ["mothers-day", "birthday", "romance"],
        "care": {
            "watering_frequency_days": 5,
            "temperature_range": "12-16°C",
            "light_requirement": "bright_indirect",
            "humidity_level": "medium",
            "soil_type": "Повітропроникна суміш торфу та піску для бульбових рослин",
            "stem_cutting_tips": "Цикламен любить прохолоду (12-16°C). Поливайте виключно через піддон, щоб вода не потрапляла на верхівку бульби.",
            "florist_secret": "Не ставте цикламен поруч з батареями опалення: надмірне тепло призводить до швидкого пожовтіння листя та скидання бутонів.",
            "fun_fact": "Стародавні римляни висаджували цикламени як природні обереги біля входу до маєтків."
        }
    },

   
    {
        "name": "Лаванда",
        "latin_name": "Lavandula angustifolia",
        "category_slug": "dried-flowers",
        "description": "Ароматний букет гірської лаванди з насиченими фіолетовими колосками та чарівним заспокійливим ароматом. Символ чистоти, душевного спокою, вірності та гармонії.",
        "fun_fact": "Запах лаванди має науково доведений седативний ефект, знижуючи рівень кортизолу та нормалізуючи сон.",
        "difficulty_level": "easy",
        "image_url": "https://images.unsplash.com/photo-1611625105602-42ee06be977e?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8bGF2YW5kZXJ8ZW58MHx8MHx8fDA%3D&utm_source=chatgpt.com",
        "occasions": ["romance", "birthday", "mothers-day"],
        "care": {
            "watering_frequency_days": 0,
            "temperature_range": "15-25°C",
            "light_requirement": "shade",
            "humidity_level": "low",
            "soil_type": "Сухе середовище без ґрунту та води",
            "stem_cutting_tips": "Не потребує води взагалі. Тримайте букет у сухій вазі подалі від підвищеної вологості та ванних кімнат.",
            "florist_secret": "Щоб освіжити аромат через рік, достатньо злегка стиснути суцвіття пальцями — капсули ефірної олії відкриються з новою силою.",
            "fun_fact": "У Стародавньому Римі лаванду додавали до купалень, звідки й походить її назва від латинського 'lavare' — мити."
        }
    },
    {
        "name": "Евкаліпт",
        "latin_name": "Eucalyptus cinerea",
        "category_slug": "dried-flowers",
        "description": "Сріблясто-зелені гілочки з округлим листям та свіжим ментолово-смолистим ароматом. Незамінний елемент весільної та сучасної інтер'єрної флористики.",
        "fun_fact": "Евкаліпт чудово сохне природним шляхом, зберігаючи свою сріблясту форму та антибактеріальний аромат роками.",
        "difficulty_level": "easy",
        "image_url": "https://plus.unsplash.com/premium_photo-1674248075482-ac8d5f4ea6f6?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8ZXVjYWx5cHR1c3xlbnwwfHwwfHx8MA%3D%3D&utm_source=chatgpt.com",
        "occasions": ["wedding", "business", "birthday"],
        "care": {
            "watering_frequency_days": 0,
            "temperature_range": "15-24°C",
            "light_requirement": "shade",
            "humidity_level": "low",
            "soil_type": "Суха ваза без води",
            "stem_cutting_tips": "Може стояти як свіжим у воді, так і висихати у порожній вазі без втрати своєї привабливої фактури.",
            "florist_secret": "Під час висихання не змінюйте положення гілочок, щоб вони зафіксувалися у витонченій природній формі.",
            "fun_fact": "Евкаліпт родом з Австралії, де є основною та практично єдиною їжею кумедних ведмедиків коала."
        }
    },
    {
        "name": "Целозія",
        "latin_name": "Celosia argentea",
        "category_slug": "dried-flowers",
        "description": "Екстравагантна квітка з оксамитовими пір'ястими суцвіттями насичених коралових, багряних і золотих тонів. Символ хоробрості, неординарності та пристрасті.",
        "fun_fact": "Назва рослини походить від грецького 'kelos' (палаючий або полум'яний) через схожість її суцвіть на язики вогню.",
        "difficulty_level": "easy",
        "image_url": "https://images.unsplash.com/photo-1745758585657-4bd42031d97e?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8Q2Vsb3NpYSUyMGFyZ2VudGVhfGVufDB8fDB8fHww",
        "occasions": ["birthday", "wedding"],
        "care": {
            "watering_frequency_days": 0,
            "temperature_range": "16-25°C",
            "light_requirement": "shade",
            "humidity_level": "low",
            "soil_type": "Сухий вентильований простір",
            "stem_cutting_tips": "Сушіть суцвіття, підвісивши їх голівками донизу у темному сухому приміщенні протягом двох тижнів.",
            "florist_secret": "Суха целозія зберігає свій вогняний колір понад два роки, якщо оберігати її від прямих сонячних променів.",
            "fun_fact": "У країнах Західної Африки молоде листя деяких видів целозії готують як поживний вітамінний шпинат."
        }
    },
    {
        "name": "Протея",
        "latin_name": "Protea cynaroides",
        "category_slug": "dried-flowers",
        "description": "Монументальна королівська квітка з Південної Африки з великою чашею з рожевих шкірястих пелюсток. Символ мужності, трансформації, величі та стійкості.",
        "fun_fact": "Протея є національною емблемою Південно-Африканської Республіки та зображена на її монетах і гербі.",
        "difficulty_level": "medium",
        "image_url": "https://media.istockphoto.com/id/154957156/ru/%D1%84%D0%BE%D1%82%D0%BE/%D0%BC%D0%B0%D0%BB%D0%B5%D0%BD%D1%8C%D0%BA%D0%B8%D0%B9-prince-%D0%B2-%D1%81%D0%B0%D0%B4.jpg?s=612x612&w=0&k=20&c=T52kaYhw8zupkKL6VKByoPRAAQnN0rgQWCHFZoRt3I8=&utm_source=chatgpt.com",
        "occasions": ["business", "wedding", "birthday"],
        "care": {
            "watering_frequency_days": 0,
            "temperature_range": "15-24°C",
            "light_requirement": "shade",
            "humidity_level": "low",
            "soil_type": "Суха інтер'єрна ваза без ґрунту",
            "stem_cutting_tips": "Ідеально висихає самостійно прямо у вазі без використання будь-яких хімічних закріплювачів.",
            "florist_secret": "Протея — справжній довгожитель серед флористичного декору, її скульптурна чаша прикрашає інтер'єр роками.",
            "fun_fact": "Рослину назвав Карл Лінней на честь давньогрецького морського бога Протея, здатного змінювати свій вигляд."
        }
    },
    {
        "name": "Вербена",
        "latin_name": "Verbena bonariensis",
        "category_slug": "dried-flowers",
        "description": "Граційна повітряна рослина з мереживом крихітних лавандово-фіолетових суцвіть на витончених гілочках. Втілює легкість, чарівність, романтичність і натхнення.",
        "fun_fact": "У середньовічній Європі вербену вважали священною магічною травою, яка приносить мир і захищає від лихого ока.",
        "difficulty_level": "easy",
        "image_url": "https://media.istockphoto.com/id/484272262/ru/%D1%84%D0%BE%D1%82%D0%BE/%D0%B2%D0%B5%D1%80%D0%B1%D0%B5%D0%BD%D0%B0-bonariensis-flower.jpg?s=612x612&w=0&k=20&c=dnRgxEXUPJeUla-Hz3CWzQzm0QXeIXk8SHy9nKh7Iro=&utm_source=chatgpt.com",
        "occasions": ["birthday", "romance"],
        "care": {
            "watering_frequency_days": 0,
            "temperature_range": "16-24°C",
            "light_requirement": "shade",
            "humidity_level": "low",
            "soil_type": "Сухий вентильований декор",
            "stem_cutting_tips": "Сушіть невеликими пучками у сухому затіненому місці для збереження фіолетового пігменту суцвіть.",
            "florist_secret": "У сухоцвітних композиціях створює неперевершену текстурну глибину та повітряний прованський шарм.",
            "fun_fact": "Суцвіття вербени бонарської в саду є головним магнітом для рідкісних видів метеликів."
        }
    },
    {
        "name": "Гіпсофіла",
        "latin_name": "Gypsophila paniculata",
        "category_slug": "dried-flowers",
        "description": "Невагома квітуча хмаринка з тисяч мініатюрних білосніжних зірочок. Символ невинності, вічного кохання, ніжності та витонченої легкості.",
        "fun_fact": "В англомовних країнах гіпсофілу поетично називають 'Baby's Breath' (дихання дитини) за її неперевершену ніжність.",
        "difficulty_level": "easy",
        "image_url": "https://images.unsplash.com/photo-1650805073031-e7991f380253?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D",
        "occasions": ["wedding", "romance", "birthday"],
        "care": {
            "watering_frequency_days": 0,
            "temperature_range": "15-25°C",
            "light_requirement": "shade",
            "humidity_level": "low",
            "soil_type": "Суха інтер'єрна ваза без води",
            "stem_cutting_tips": "Після висихання у сухій вазі гіпсофіла зберігає форму ажурної мереживної хмарки на багато років.",
            "florist_secret": "Не ставте суху гіпсофілу під прямі сонячні промені, щоб білосніжні пелюстки не пожовтіли з часом.",
            "fun_fact": "Гіпсофіла любить ґрунти, багаті на гіпс та вапно, звідки й походить її ботанічна назва."
        }
    },
    {
        "name": "Статиця",
        "latin_name": "Limonium sinuatum",
        "category_slug": "dried-flowers",
        "description": "Класичний нев'янучий сухоцвіт з крилатими пагонами та щільними суцвіттями яскраво-фіолетових, рожевих і жовтих паперових квіточок. Символ пам'яті та вічності.",
        "fun_fact": "Чашолистки статиці мають природну плівчасту структуру, яка зовсім не містить вологи і тому ніколи не в'яне.",
        "difficulty_level": "easy",
        "image_url": "https://plus.unsplash.com/premium_photo-1677597797674-2cb6a093cea7?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D",
        "occasions": ["birthday", "business"],
        "care": {
            "watering_frequency_days": 0,
            "temperature_range": "15-25°C",
            "light_requirement": "shade",
            "humidity_level": "low",
            "soil_type": "Сухе місце без вологи",
            "stem_cutting_tips": "Зрізайте у фазі повного розкриття суцвіть і висушуйте у темному сухому місці.",
            "florist_secret": "Статиця абсолютно стійка до вицвітання і зберігає природну соковитість кольору до трьох років.",
            "fun_fact": "У природі статиця росте на засолених морських узбережжях та степових солончаках."
        }
    },
    {
        "name": "Кермек",
        "latin_name": "Limonium gmelinii",
        "category_slug": "dried-flowers",
        "description": "Ажурний степовий сухоцвіт з каскадом дрібних бузкових квіточок, що утворює розкішну пухнасту волоть. Уособлює безмежність степового простору та стійкість духу.",
        "fun_fact": "Висушений кущ кермека восени під дією вітру відривається і котиться степом, утворюючи знамените 'перекотиполе'.",
        "difficulty_level": "easy",
        "image_url": "https://media.gettyimages.com/id/2149354194/photo/statice-limonium-sinuatum-violet-flower-and-gypsophila-paniculata-l-caryophyllaceae-white.jpg?s=612x612&w=0&k=20&c=4-U_69XPpYcEseUiRAN4F1YDSXLAjEtDxaWVjqGCHH4=",
        "occasions": ["wedding", "birthday"],
        "care": {
            "watering_frequency_days": 0,
            "temperature_range": "16-25°C",
            "light_requirement": "shade",
            "humidity_level": "low",
            "soil_type": "Суха декоративна місткість",
            "stem_cutting_tips": "Не потребує жодного зволоження. Зберігайте в сухій вазі як самостійний букет або фоновий елемент.",
            "florist_secret": "Кермек слугує чудовим об'ємним наповнювачем для створення вінків у стилі бохо та рустик.",
            "fun_fact": "Коріння кермека містить велику кількість танінів, які здавна використовували для дублення шкіри."
        }
    },
    {
        "name": "Фізаліс",
        "latin_name": "Physalis alkekengi",
        "category_slug": "dried-flowers",
        "description": "Яскравий осінній сухоцвіт з витонченими паперовими ліхтариками насиченого вогняно-помаранчевого кольору. Символ затишку, достатку, тепла та захисту.",
        "fun_fact": "Усередині кожного помаранчевого ліхтарика ховається невелика кругла ягідка, захищена від негоди.",
        "difficulty_level": "easy",
        "image_url": "https://images.unsplash.com/photo-1596411754250-72bce519ed8c?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D",
        "occasions": ["birthday", "business"],
        "care": {
            "watering_frequency_days": 0,
            "temperature_range": "15-25°C",
            "light_requirement": "shade",
            "humidity_level": "low",
            "soil_type": "Суха інтер'єрна композиція",
            "stem_cutting_tips": "Зрізайте гілочки, коли ліхтарики набудуть яскравого помаранчевого кольору, і видаляйте листя перед сушінням.",
            "florist_secret": "Гілочки фізаліса можна висушити як прямими, так і злегка зігнутими для надання композиції динаміки.",
            "fun_fact": "Назва 'Physalis' походить від грецького слова 'physa' (міхур) через характерну здуту форму чашечки."
        }
    },
    {
        "name": "Лунарія",
        "latin_name": "Lunaria annua",
        "category_slug": "dried-flowers",
        "description": "Загадкова рослина, відома як 'срібний рубель' або 'місячник', з перламутровими напівпрозорими перетинками стручків. Символізує чесність, світло та містичну красу.",
        "fun_fact": "У Франції лунарію називають 'монетою Папи', а в багатьох країнах сухі стручки клали в гаманець для приваблення грошей.",
        "difficulty_level": "easy",
        "image_url": "https://media.istockphoto.com/id/490771619/ru/%D1%84%D0%BE%D1%82%D0%BE/%D1%86%D0%B2%D0%B5%D1%82%D1%8B-%D0%B2-%D1%86%D0%B2%D0%B5%D1%82%D1%83%D1%89%D0%B8%D0%B9-lunaria-rediviva.jpg?s=612x612&w=0&k=20&c=63n6GT0g1K-dXz4cljHC6skplaxzZHNjxzNxr6mfing=",
        "occasions": ["wedding", "birthday"],
        "care": {
            "watering_frequency_days": 0,
            "temperature_range": "15-24°C",
            "light_requirement": "shade",
            "humidity_level": "low",
            "soil_type": "Суха ваза без рідини",
            "stem_cutting_tips": "Акуратно потріть пальцями дозрілі стручки, щоб зняти зовнішні стулки і звільнити сріблясті перламутрові перетинки.",
            "florist_secret": "Перламутрові диски місячника дивовижно відбивають електричне світло, створюючи казкове мерехтіння у вечірньому інтер'єрі.",
            "fun_fact": "Латинська назва Lunaria походить від слова 'luna' (місяць), вказуючи на круглу форму та сяйво перегородок."
        }
    },
    {
        "name": "Краспедія",
        "latin_name": "Craspedia globosa",
        "category_slug": "dried-flowers",
        "description": "Оригінальні графічні золотисто-жовті кульки на міцних струнких стеблах, відомі як 'барабанні палички'. Символізують життєрадісність, креативність та оптимізм.",
        "fun_fact": "Краспедія природно висихає прямо на стеблі, не втрачаючи ідеальної форми кулі та насиченого сонячного кольору.",
        "difficulty_level": "easy",
        "image_url": "https://plus.unsplash.com/premium_photo-1664304324124-e2fa2361c20f?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D",
        "occasions": ["birthday", "business"],
        "care": {
            "watering_frequency_days": 0,
            "temperature_range": "15-25°C",
            "light_requirement": "shade",
            "humidity_level": "low",
            "soil_type": "Сухий інтер'єрний декор",
            "stem_cutting_tips": "Просто поставте стебла краспедії у суху вазу — вона висохне самостійно за кілька днів.",
            "florist_secret": "Краспедія ідеально підходить для створення сучасних геометричних та мінімалістичних інтер'єрних аранжувань.",
            "fun_fact": "У дикій природі краспедія росте в Альпах Австралії та Нової Зеландії на висоті понад 1000 метрів."
        }
    },
    {
        "name": "Амарант",
        "latin_name": "Amaranthus caudatus",
        "category_slug": "dried-flowers",
        "description": "Каскадний ефектний сухоцвіт з довгими оксамитовими суцвіттями-хвостами рубінового кольору. Втілює безсмертя, вірність, внутрішню міць і величність.",
        "fun_fact": "Стародавні ацтеки вважали амарант священною зерновою культурою та символом вічного життя.",
        "difficulty_level": "easy",
        "image_url": "https://plus.unsplash.com/premium_photo-1663962390305-718957d7e8ac?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D",
        "occasions": ["wedding", "birthday"],
        "care": {
            "watering_frequency_days": 0,
            "temperature_range": "16-24°C",
            "light_requirement": "shade",
            "humidity_level": "low",
            "soil_type": "Сухе темне приміщення",
            "stem_cutting_tips": "Сушіть підвішеним суцвіттями донизу, щоб звисаючі китиці зафіксувалися у красивому рівному положенні.",
            "florist_secret": "Назва рослини походить від грецького 'amarantos' — нев'янучий, що повністю підтверджується її надзвичайною довговічністю.",
            "fun_fact": "Зерна амаранту містять сквален — цінний антиоксидант, який використовується в сучасній косметології."
        }
    },
    {
        "name": "Ковила",
        "latin_name": "Stipa tenuissima",
        "category_slug": "dried-flowers",
        "description": "М'яка шовковиста степова трава з довгими пір'ястими остями, що витончено колишуться від найменшого подиху вітру. Символ свободи, простору і природної грації.",
        "fun_fact": "У народі ковилу називають 'шовковою травою' за надзвичайну ніжність її остей на дотик.",
        "difficulty_level": "easy",
        "image_url": "https://media.gettyimages.com/id/517561984/photo/mexican-feather-grass-is-blowing-in-the-wind.jpg?s=612x612&w=0&k=20&c=ytMkBTUmopyC9zqdKOTIjNC9O4CPAOOr40O-h2C4RPg=",
        "occasions": ["wedding", "business"],
        "care": {
            "watering_frequency_days": 0,
            "temperature_range": "15-25°C",
            "light_requirement": "shade",
            "humidity_level": "low",
            "soil_type": "Сухий букет без води",
            "stem_cutting_tips": "Збирайте ковилу до початку розлітання насіння та злегка зафіксуйте ості лаком для волосся, щоб уникнути осипання.",
            "florist_secret": "Ковила додає будь-якому букету сухоцвітів м'якості, динаміки та сучасного бохо-шику.",
            "fun_fact": "Ковила є типовою рослиною українських заповідних степів, зокрема всесвітньо відомої 'Асканії-Нова'."
        }
    },
    {
        "name": "Геліхризум",
        "latin_name": "Helichrysum bracteatum",
        "category_slug": "dried-flowers",
        "description": "Яскравий сухоцвіт-безсмертник з різнокольоровими жорсткими суцвіттями, пелюстки якого шелестять як тонкий папір. Символізує незгасну пам'ять і стійкість.",
        "fun_fact": "Пелюстки геліхризуму насправді є сухими лусочками обгортки, тому вони не втрачають форму і колір десятиліттями.",
        "difficulty_level": "easy",
        "image_url": "https://images.unsplash.com/photo-1753109112481-96ae50417867?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D",
        "occasions": ["birthday", "mothers-day"],
        "care": {
            "watering_frequency_days": 0,
            "temperature_range": "15-25°C",
            "light_requirement": "shade",
            "humidity_level": "low",
            "soil_type": "Сухий вазон без води",
            "stem_cutting_tips": "Зрізайте у напіврозкритому стані, оскільки під час сушіння суцвіття продовжує розкриватися ще більше.",
            "florist_secret": "Не піддавайте сухі квіти впливу пари чи конденсату, щоб суцвіття не закривалися назад у бутони.",
            "fun_fact": "Назва походить від грецьких слів 'helios' (сонце) та 'chrysos' (золото)."
        }
    },
    {
        "name": "Пшениця декоративна",
        "latin_name": "Triticum aestivum",
        "category_slug": "dried-flowers",
        "description": "Золотаві колоски добірної пшениці з довгими рівними остями. Сакральний символ українського достатку, родючості, хліба, миру та щедрості рідної землі.",
        "fun_fact": "Колосок пшениці здавна був головним елементом українського традиційного різдвяного дідуха.",
        "difficulty_level": "easy",
        "image_url": "https://images.unsplash.com/photo-1595266815066-da829b4de7e4?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D",
        "occasions": ["business", "birthday"],
        "care": {
            "watering_frequency_days": 0,
            "temperature_range": "15-25°C",
            "light_requirement": "shade",
            "humidity_level": "low",
            "soil_type": "Суха ваза чи сніп без рідини",
            "stem_cutting_tips": "Зберігайте у сухому приміщенні з гарною вентиляцією для уникнення відсирівання.",
            "florist_secret": "Колоски пшениці чудово поєднуються з лавандою та польовими квітами, створюючи автентичний український оберіг.",
            "fun_fact": "Пшениця є однією з найперших одомашнених рослин в історії людської цивілізації, її вирощують понад 10 тисяч років."
        }
    },

  
    {
        "name": "Стреліція",
        "latin_name": "Strelitzia reginae",
        "category_slug": "exotic-flowers",
        "description": "Легендарна південноафриканська квітка 'райський птах' з дивовижними суцвіттями помаранчевого та сапфірово-синього кольорів. Символізує свободу, велич і успіх.",
        "fun_fact": "У природі стреліцію запилюють крихітні пташки-нектарниці, які сідають на блакитні пелюстки, що діють як важіль для відкриття пиляків.",
        "difficulty_level": "hard",
        "image_url": "https://images.unsplash.com/photo-1699043787902-84a29a6a286a?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D",
        "occasions": ["business", "birthday", "wedding"],
        "care": {
            "watering_frequency_days": 5,
            "temperature_range": "18-24°C",
            "light_requirement": "bright_indirect",
            "humidity_level": "high",
            "soil_type": "Поживний дренований ґрунт з глиною та перегноєм",
            "stem_cutting_tips": "Потребує багато розсіяного світла та помірного поливу після підсихання верхнього шару ґрунту.",
            "florist_secret": "Зрізана стреліція здатна послідовно випускати нові квіти з одного човникоподібного приквітка, якщо акуратно діставати їх пінцетом.",
            "fun_fact": "Квітка названа на честь королеви Шарлотти, уродженої герцогині Мекленбург-Стреліцької, дружини короля Великобританії Георга III."
        }
    },
    {
        "name": "Геліконія",
        "latin_name": "Heliconia rostrata",
        "category_slug": "exotic-flowers",
        "description": "Вражаюча тропічна рослина з каскадними звисаючими суцвіттями, схожими на яскраві червоно-жовті клішні омара. Символ екзотики, життєлюбства та непереборної сили.",
        "fun_fact": "Суцвіття геліконії настільки міцні та воскові, що можуть триматися свіжими на рослині до пів року.",
        "difficulty_level": "hard",
        "image_url": "https://images.unsplash.com/photo-1720425180820-e1f4bd0141a5?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D",
        "occasions": ["business", "birthday"],
        "care": {
            "watering_frequency_days": 4,
            "temperature_range": "21-26°C",
            "light_requirement": "bright_indirect",
            "humidity_level": "high",
            "soil_type": "Багатий органікою вологоємний субстрат",
            "stem_cutting_tips": "Любить високу вологість повітря та тепло. Не переносить охолодження нижче 16°C.",
            "florist_secret": "У вазі з водою геліконія не потребує підрізання частіше ніж раз на тиждень завдяки щільній шкірці стебла.",
            "fun_fact": "Назва походить від гори Гелікон у Греції, яка вважалася священним притулком давньогрецьких муз."
        }
    },
    {
        "name": "Пасифлора",
        "latin_name": "Passiflora caerulea",
        "category_slug": "exotic-flowers",
        "description": "Казкова ліана з неймовірно складною будовою квітки з біло-блакитними нитками корони, відома як 'кавалерська зірка'. Символ віри, натхнення та глибини світобудови.",
        "fun_fact": "Християнські місіонери вбачали в елементах будови квітки символи Страстей Христових: 10 пелюсток — 10 апостолів, нитки — терновий вінець.",
        "difficulty_level": "medium",
        "image_url": "https://images.unsplash.com/photo-1628341423248-4b8c5c51a3cd?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D",
        "occasions": ["romance", "birthday"],
        "care": {
            "watering_frequency_days": 3,
            "temperature_range": "19-24°C",
            "light_requirement": "direct_sun",
            "humidity_level": "medium",
            "soil_type": "Поживний суглинок з додаванням піску та торфу",
            "stem_cutting_tips": "Потребує міцної опори для активного плетіння та великої кількості сонячного світла для цвітіння.",
            "florist_secret": "Помірне обмеження об'єму горщика стимулює закладку більшої кількості дивовижних квітів замість зеленої маси.",
            "fun_fact": "Багато видів пасифлори утворюють смачні екзотичні плоди, найвідомішим з яких є маракуя."
        }
    },
    {
        "name": "Бромелія",
        "latin_name": "Guzmania lingulata",
        "category_slug": "exotic-flowers",
        "description": "Тропічна красуня з лійкоподібною розеткою листя та палаючим неоновим суцвіттям у центрі. Уособлює гостинність, радість, життєву силу та екзотичний колорит.",
        "fun_fact": "У тропічних лісах у лійках бромелій накопичується дощова вода, в якій утворюються цілі мініатюрні екосистеми з пуголовками та комахами.",
        "difficulty_level": "medium",
        "image_url": "https://images.unsplash.com/photo-1747734519388-fe79575add06?q=80&w=1035&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D",
        "occasions": ["business", "birthday"],
        "care": {
            "watering_frequency_days": 5,
            "temperature_range": "20-25°C",
            "light_requirement": "bright_indirect",
            "humidity_level": "high",
            "soil_type": "Легкий пухкий субстрат з подрібненої кори, торфу та сфагнуму",
            "stem_cutting_tips": "Поливати слід безпосередньо в центр листової розетки м'якою теплою водою.",
            "florist_secret": "Після цвітіння материнська розетка відмирає, даючи життя кільком молодим бічним пагонам-діткам.",
            "fun_fact": "Найвідомішим представником родини бромелієвих є звичайний їстівний ананас."
        }
    },
    {
        "name": "Медініла",
        "latin_name": "Medinilla magnifica",
        "category_slug": "exotic-flowers",
        "description": "Королева тропічних оранжерей з масивними звисаючими гронами рожевих дзвіночків під ніжними приквітками. Символ царської розкоші, елегантності та вишуканого смаку.",
        "fun_fact": "Король Бельгії Бодуен настільки захоплювався медінілою, що наказав зобразити її на банкноті у 10 000 бельгійських франків.",
        "difficulty_level": "hard",
        "image_url": "https://images.unsplash.com/photo-1685790742062-7d27e91f1d38?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D",
        "occasions": ["wedding", "birthday", "romance"],
        "care": {
            "watering_frequency_days": 5,
            "temperature_range": "20-25°C",
            "light_requirement": "bright_indirect",
            "humidity_level": "high",
            "soil_type": "Пухкий субстрат для орхідей та епіфітів",
            "stem_cutting_tips": "Дуже вимоглива до вологості повітря: вимагає щоденного обприскування та стабільної температури без протягів.",
            "florist_secret": "У період закладання бутонів ніколи не перевертайте і не переставляйте горщик на інше місце.",
            "fun_fact": "У природі медініла росте на Філіппінських островах як напівчагарниковий епіфіт у розвилках стовбурів дерев."
        }
    },
    {
        "name": "Плюмерія",
        "latin_name": "Plumeria rubra",
        "category_slug": "exotic-flowers",
        "description": "Божественна квітка тропічних островів з товстими восковими пелюстками та п'янким солодким ароматом франжипані. Символ безсмертя, жіночності, любові та витонченості.",
        "fun_fact": "Саме з ароматних квітів плюмерії на Гавайських островах плетуть традиційні вітальні намиста-гірлянди 'леї'.",
        "difficulty_level": "medium",
        "image_url": "https://images.unsplash.com/photo-1640818938000-cd9ea9c92518?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D",
        "occasions": ["romance", "wedding", "birthday"],
        "care": {
            "watering_frequency_days": 5,
            "temperature_range": "22-27°C",
            "light_requirement": "direct_sun",
            "humidity_level": "medium",
            "soil_type": "Поживний дренований субстрат з піском і перлітом",
            "stem_cutting_tips": "Потребує прямого сонячного світла мінімум 4-6 годин на добу для формування бутонів.",
            "florist_secret": "Аромат плюмерії стає найбільш насиченим у вечірній та нічний час для приваблення нічних метеликів-запилювачів.",
            "fun_fact": "Квіти плюмерії зберігають свіжість і солодкий аромат кілька днів навіть після того, як їх зірвали з гілки."
        }
    },
    {
        "name": "Гібіскус",
        "latin_name": "Hibiscus rosa-sinensis",
        "category_slug": "exotic-flowers",
        "description": "Розкішна 'китайська троянда' з величезними полум'яно-червоними шовковистими пелюстками та довгим витонченим товкачем. Уособлює пристрасть, сміливість, красу та славу.",
        "fun_fact": "Гібіскус є національною квіткою Малайзії, де його зображення прикрашає державну валюту.",
        "difficulty_level": "medium",
        "image_url": "https://images.unsplash.com/photo-1567990989224-6441e1483ac8?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D",
        "occasions": ["birthday", "romance"],
        "care": {
            "watering_frequency_days": 3,
            "temperature_range": "19-25°C",
            "light_requirement": "bright_indirect",
            "humidity_level": "medium",
            "soil_type": "Поживна суміш дернової землі, перегною та торфу",
            "stem_cutting_tips": "Потребує щедрого поливу в період цвітіння та яскравого освітлення. Влітку корисно виносити на відкрите повітря.",
            "florist_secret": "Хоча кожна квітка живе всього один день, здоровий кущ щоранку розпускає нові бутони з весни до осені.",
            "fun_fact": "З висушених пелюсток спорідненого суданського гібіскуса (розели) заварюють освіжаючий рубіновий чай каркаде."
        }
    },
    {
        "name": "Кальцеолярія",
        "latin_name": "Calceolaria herbeohybrida",
        "category_slug": "exotic-flowers",
        "description": "Незвичайна екзотична рослина з оригінальними квіточками, схожими на яскраві крапчасті черевички або гаманці. Символ багатства, дива, грайливості та сюрпризу.",
        "fun_fact": "Назва рослини походить від латинського 'calceolus' — маленький черевичок.",
        "difficulty_level": "hard",
        "image_url": "https://media.gettyimages.com/id/1257659173/photo/calceolaria.jpg?s=612x612&w=0&k=20&c=KIQG5D4lcOqDH8BHI3RrdiHZAIa1YgTyi-OSy2VQsVI=",
        "occasions": ["birthday", "mothers-day"],
        "care": {
            "watering_frequency_days": 3,
            "temperature_range": "14-17°C",
            "light_requirement": "bright_indirect",
            "humidity_level": "high",
            "soil_type": "Пухкий слабокислий субстрат з піском і торфом",
            "stem_cutting_tips": "Любить прохолодне повітря (14-17°C) та рівномірне зволоження ґрунту без застою води в піддоні.",
            "florist_secret": "Ніколи не обприскуйте квіти та листя водою — опушена поверхня черевичків може вкритися плямами.",
            "fun_fact": "Батьківщиною диких кальцеолярій є гори Анди в Південній Америці."
        }
    },
    {
        "name": "Такка",
        "latin_name": "Tacca chantrieri",
        "category_slug": "exotic-flowers",
        "description": "Одна з найбільш таємничих рослин світу, відома як 'квітка-летюча миша' або 'чорна орхідея' з глибокими чорно-фіолетовими приквітками та довгими вусиками. Символ містики, магії та винятковості.",
        "fun_fact": "Довгі ниткоподібні вуса суцвіття такки можуть досягати 40-50 см у довжину, спадаючи навколо бутона.",
        "difficulty_level": "hard",
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRujJ_RZI1hwViyxr_w4FtrO6MQa3x82II_s1k0mniQsw&s=10",
        "occasions": ["business", "birthday"],
        "care": {
            "watering_frequency_days": 4,
            "temperature_range": "21-27°C",
            "light_requirement": "partial_shade",
            "humidity_level": "high",
            "soil_type": "Повітропроникна суміш для орхідей з торфом і деревним вугіллям",
            "stem_cutting_tips": "Потребує високої вологості тропічного лісу (понад 70%) і затінення від прямого сонця.",
            "florist_secret": "Такка погано переносить пересушування коренів, тому ґрунт повинен завжди бути злегка вологим, але не заболоченим.",
            "fun_fact": "У Південно-Східній Азії з бульб такки місцеве населення добуває харчовий крохмаль."
        }
    },
    {
        "name": "Орхідея Ванда",
        "latin_name": "Vanda coerulea",
        "category_slug": "exotic-flowers",
        "description": "Королева серед орхідей з дивовижними сапфірово-блакитними або пурпуровими сітчастими квітами неймовірної краси. Символ шляхетності, рідкісності, вищої розкоші та витонченості.",
        "fun_fact": "Ванда здатна жити і цвісти взагалі без субстрату — її вирощують у підвісних кошиках або скляних вазах із відкритим корінням.",
        "difficulty_level": "hard",
        "image_url": "https://images.unsplash.com/photo-1751444041692-381ca02d6bb4?q=80&w=3131&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D",
        "occasions": ["wedding", "romance", "business"],
        "care": {
            "watering_frequency_days": 2,
            "temperature_range": "20-26°C",
            "light_requirement": "bright_indirect",
            "humidity_level": "high",
            "soil_type": "Вирощується з відкритим повітряним корінням у підвісному кошику без ґрунту",
            "stem_cutting_tips": "Коріння щодня або через день замочують у ємності з теплою водою на 20-30 хвилин, після чого дають воді повністю стекти.",
            "florist_secret": "Для регулярного цвітіння ванді потрібен перепад між денною та нічною температурою в 4-6 градусів.",
            "fun_fact": "Блакитна ванда була відкрита в лісах Гімалаїв ботаніком Вільямом Гріффітом у 1837 році."
        }
    },
]
