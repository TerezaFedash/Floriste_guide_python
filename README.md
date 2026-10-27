### Крок 1. Клонування репозиторію та перехід у каталог
```bash
git clone <URL_репозиторію>
cd zvit_python
```

### Крок 2. Створення та активація віртуального середовища
```bash
# macOS / Linux:
python3 -m venv venv
source venv/bin/activate

# Windows:
python -m venv venv
venv\Scripts\activate
```

### Крок 3. Встановлення залежностей із зафіксованими версіями 
```bash
pip install -r requirements.txt
```

### Крок 4. Налаштування змінних оточення 
Скопіюйте шаблонний файл `.env.example` у новий файл `.env`:
```bash
cp .env.example .env
```

Відкрийте файл `.env` та налаштуйте параметри:
```env
SECRET_KEY=your-django-super-secret-key-change-in-production
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

# Налаштування СУБД MySQL (В2.1, В2.2)
DB_ENGINE=django.db.backends.mysql
DB_NAME=florist_db
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_HOST=127.0.0.1
DB_PORT=3306
```

### Крок 5. Створення бази даних у MySQL
Увійдіть у консоль MySQL клієнта та створіть базу:
```sql
CREATE DATABASE florist_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### Крок 6. Застосування міграцій та data-міграції 
```bash
python manage.py migrate
```
> Міграція автоматично застосує початкову схему та запустить **Data-міграцію (RunPython)** `0002_seed_initial_data`, яка автоматично наповнить базу тестовими категоріями, подіями, сортами квітів, довідниками з догляду, групами прав та користувачами!

### Крок 7. Запуск сервера розробки
```bash
python manage.py runserver
```
Відкрийте браузер за адресою: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 👤 4. Демонстраційні облікові записи (В7.1, В7.4)

У системі створено попередньо налаштовані користувачі з різними ролями та правами:

| Роль | Логін | Пароль | Можливості в системі |
| :--- | :--- | :--- | :--- |
| **Старший Флорист** *(привілейована роль)* | `olena_florist` | `florist12345` | Складання довідників догляду, доступ до закритої аналітичної панелі `/florist-dashboard/`, повне редагування каталогу. |
| **Клієнт / Покупець** | `ivan_client` | `client12345` | Перегляд каталогу, додавання в обране, замовлення консультації, додавання власних записів. |
| **Головний Адміністратор** | `admin` | `admin12345` | Повний доступ до стандартної панелі керування Django: `/admin/`. |

---
