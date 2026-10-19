"""
Django settings for florist_project.
Навчальний проєкт для практики: 'Довідник Флориста'.
Розроблено відповідно до вимог В1.1, В2.1, В2.2, Д5, Д7.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Завантаження змінних середовища з файлу .env (В2.2)
load_dotenv()

# Ініціалізація PyMySQL як драйвера MySQLdb для безшовної роботи з MySQL СУБД (В2.1)
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError:
    pass

# Базова директорія проєкту
BASE_DIR = Path(__file__).resolve().parent.parent

# Безпека: читання SECRET_KEY зі змінних середовища (В2.2)
SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "django-insecure-florist-guide-college-practice-secret-key-2026-super-safe"
)

# Режим налагодження
DEBUG = os.getenv("DEBUG", "True").lower() in ("true", "1", "yes")

# Дозволені хости
ALLOWED_HOSTS = [h.strip() for h in os.getenv("ALLOWED_HOSTS", "127.0.0.1,localhost").split(",") if h.strip()]

# Реєстрація застосунків (В1.1)
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Д5: Django Debug Toolbar для оптимізації та контролю N+1 запитів
    "debug_toolbar",

    # Власний застосунок предметної області
    "catalog.apps.CatalogConfig",
]

# Проміжне програмне забезпечення (Middleware) (Д5, Д7)
MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",  # Д5: перевірка SQL-запитів
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # Д7: Власний Middleware для підтримки теми (світла/темна) та моніторингу часу відповіді
    "catalog.middleware.ThemeAndTimingMiddleware",
]

ROOT_URLCONF = "florist_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # Глобальний контекстний процесор для флористичного довідника
                "catalog.context_processors.florist_global_context",
            ],
        },
    },
]

WSGI_APPLICATION = "florist_project.wsgi.application"

# База даних (В2.1, В2.2)
# Конфігурація MySQL з обліковими даними з .env; можливість тестування з sqlite3
DB_ENGINE = os.getenv("DB_ENGINE", "django.db.backends.mysql")

if DB_ENGINE == "django.db.backends.mysql":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": os.getenv("DB_NAME", "florist_db"),
            "USER": os.getenv("DB_USER", "root"),
            "PASSWORD": os.getenv("DB_PASSWORD", ""),
            "HOST": os.getenv("DB_HOST", "127.0.0.1"),
            "PORT": os.getenv("DB_PORT", "3306"),
            "OPTIONS": {
                "charset": "utf8mb4",
                "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
            },
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# Валідація паролів
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Локалізація (українська мова та часовий пояс Києва)
LANGUAGE_CODE = "uk"
TIME_ZONE = "Europe/Kyiv"
USE_I18N = True
USE_TZ = True

# Статичні файли (CSS, JavaScript, Images) (В4.2)
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

# Медіа-файли
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Налаштування перенаправлень автентифікації (В7.1)
LOGIN_URL = "catalog:login"
LOGIN_REDIRECT_URL = "catalog:flower_list"
LOGOUT_REDIRECT_URL = "catalog:home"

# Д5: Налаштування для Django Debug Toolbar
INTERNAL_IPS = [
    "127.0.0.1",
    "localhost",
]
