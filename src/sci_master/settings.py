"""
Настройки проекта SciMaster
Copyright (c) 2025 Artem Fomin
"""

import os
from pathlib import Path

from dotenv import load_dotenv

# ============================= БАЗОВЫЕ НАСТРОЙКИ =============================

# Базовый директория проекта (корневая папка проекта)
BASE_DIR = Path(__file__).resolve().parent.parent

# Загрузка переменных окружения из файла .env
env_path = BASE_DIR / '.env'
load_dotenv(dotenv_path=env_path)

# Секретный ключ приложения (хранится в .env)
SECRET_KEY = os.environ.get('SECRET_KEY')

# Режим отладки (включать только для разработки!)
DEBUG = os.environ.get('DEBUG', '').lower() in ['true', '1', 'yes']

# Разрешенные хосты (для production указывать конкретные домены)
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')


# =============================== БЕЗОПАСНОСТЬ ================================

# Настройки безопасности (активны ТОЛЬКО В PRODUCTION)
if not DEBUG:
    CSRF_COOKIE_SECURE = True     # Передача CSRF-токена только через HTTPS
    SESSION_COOKIE_SECURE = True  # Передача сессионных куков только через HTTPS
    SECURE_HSTS_SECONDS = 31536000  # HTTP Strict Transport Security: 1 год
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Применять HSTS для всех поддоменов
    SECURE_HSTS_PRELOAD = True    # Предзагрузка HSTS в браузерах
    SECURE_SSL_REDIRECT = True    # Перенаправлять все HTTP-запросы на HTTPS
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')  # Для прокси-серверов


# ========================= ПРИЛОЖЕНИЯ И МИДДЛВАРЫ ===========================

# Установленные приложения проекта
INSTALLED_APPS = [
    # Стандартные приложения Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Сторонние приложения
    'captcha',               # Капча
    'django_htmx',           # HTMX интеграция
    'django_bootstrap5',     # Bootstrap 5
    'sass_processor',        # Компилятор SASS/SCSS
    'widget_tweaks',         # Улучшение виджетов форм
    
    # Кастомные приложения (раскомментировать после создания)
    'home',
    'common',
    'users',
    # 'projects',
    # 'feedback',
    # 'billing',
    
    # Автоочистка неиспользуемых файлов
    'django_cleanup.apps.CleanupConfig',
]

# Промежуточные слои (обработчики запросов)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # Локализация
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_htmx.middleware.HtmxMiddleware',      # HTMX поддержка
]


# =========================== КОНФИГУРАЦИЯ ШАБЛОНОВ ==========================

# Корневой конфигуратор URL
ROOT_URLCONF = 'sci_master.urls'

# Настройки шаблонов
TEMPLATES_BASE_DIR = os.path.join(BASE_DIR, 'templates')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_BASE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# =============================== БАЗА ДАННЫХ =================================

# Конфигурация базы данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / os.environ.get('DATABASE_NAME'),
    }
}


# ============================= АУТЕНТИФИКАЦИЯ ================================

# Кастомная модель пользователя
AUTH_USER_MODEL = 'users.Profile'

# Перенаправление после входа в систему
LOGIN_REDIRECT_URL = '/'

# Валидаторы паролей
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# =========================== ИНТЕРНАЦИОНАЛИЗАЦИЯ =============================

# Языковые настройки
LANGUAGE_CODE = 'ru'                  # Язык по умолчанию
TIME_ZONE = 'Europe/Moscow'           # Часовой пояс
USE_I18N = True                       # Включение интернационализации
USE_L10N = True                       # Включение локализации
USE_TZ = True                         # Использование часовых поясов

# Поддерживаемые языки (для локализации)
LANGUAGES = [
    ('ru', 'Русский'),
    ('en', 'English'),
]

# Пути к файлам перевода
LOCALE_PATHS = [
    BASE_DIR / 'locale',
]


# =========================== СТАТИЧЕСКИЕ ФАЙЛЫ ==============================

# Конфигурация статических файлов (CSS, JavaScript, изображения)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.joinpath('static')]  # Папки со статикой
STATIC_ROOT = BASE_DIR.joinpath('staticfiles')    # Финалная сборка статики

# Обработчики поиска статических файлов
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'sass_processor.finders.CssFinder',  # Для обработки SASS
]

# Медиа-файлы (загружаемые пользователями)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.joinpath('media')


# ========================= СТОРОННИЕ БИБЛИОТЕКИ =============================

# Настройки Bootstrap 5
BOOTSTRAP5 = {
    "javascript_url": {
        "url": "/static/bootstrap/js/bootstrap.bundle.min.js",
    },
}

# Настройки иконок
DJANGO_ICONS = {
    "DEFAULT": {
        "renderer": "django_icons_bootstrap_icons.BootstrapIconRenderer"
    }
}

# Настройки капчи
CAPTCHA_LENGTH = 7                        # Длина капчи
CAPTCHA_FONT_SIZE = 26                    # Размер шрифта
CAPTCHA_2X_IMAGE = True                   # Изображение двойного разрешения
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'  # Математическая капча
CAPTCHA_NOISE_FUNCTIONS = (               # Эффекты на изображении
    'captcha.helpers.noise_arcs',         # Дуги
    'captcha.helpers.noise_dots',         # Точки
)


# ========================== ЭЛЕКТРОННАЯ ПОЧТА ===============================

# SMTP-настройки
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = 'SciMaster <info@b-model.pro>'
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', '').lower() in ['true', '1', 'yes']
EMAIL_USE_SSL = os.environ.get('EMAIL_USE_SSL', '').lower() in ['true', '1', 'yes']


# ============================== TELEGRAM =====================================

# Токен Telegram-бота
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')

# Список ID Telegram для уведомлений
USERS_TELEGRAM_ID = os.getenv('USERS_TELEGRAM_ID')
if USERS_TELEGRAM_ID:
    USERS_TELEGRAM_ID = [int(id) for id in USERS_TELEGRAM_ID.split(',')]
else:
    USERS_TELEGRAM_ID = []


# ============================= ПРОЧИЕ НАСТРОЙКИ ==============================

# Авто-поле для моделей
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Корневое приложение WSGI
WSGI_APPLICATION = 'sci_master.wsgi.application'

# Путь для хранения скомпилированных CSS-файлов
SASS_PROCESSOR_ROOT = STATIC_ROOT