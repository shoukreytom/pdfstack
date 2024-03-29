from pathlib import Path
import django_heroku
from decouple import config
import secrets  # just for testing (github ci)

import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
if os.path.exists(BASE_DIR / '.env'):
    SECRET_KEY = config('SECRET_KEY')
    DEBUG = (config('DEBUG') == "True")
    HOST = 'http://127.0.0.1:8000'
else:
    SECRET_KEY = os.environ.get('SECRET_KEY') or str(secrets.token_hex(24))
    DEBUG = (os.environ.get('DEBUG_VALUE') == "True")
    HOST = 'https://pdfstack.herokuapp.com'

ALLOWED_HOSTS = ['pdfstack.herokuapp.com', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # local apps
    'books.apps.BooksConfig',
    'users.apps.UsersConfig',
    #3rd party apps
    'crispy_forms',
    'import_export',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTH_USER_MODEL = 'users.User'
ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates', ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'books.context_processors.get_books',
                'books.context_processors.get_upload_form',
                'books.context_processors.get_host',
                'users.context_processors.check_email_verification',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static', ]
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
LOGIN_URL = 'users:login'
LOGIN_REDIRECT_URL = 'home'
CRISPY_TEMPLATE_PACK = 'bootstrap4'
# SECURE_SSL_REDIRECT = True
X_FRAME_OPTIONS = 'SAMEORIGIN'

# blackblaze storage
if not DEBUG:
    DEFAULT_FILE_STORAGE = 'django_b2.storage.B2Storage'
    B2_APP_KEY_ID = os.environ.get('B2_APP_KEY_ID')
    B2_APP_KEY = os.environ.get('B2_APP_KEY')
    B2_BUCKET_NAME = os.environ.get('B2_BUCKET_NAME')

# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587

if os.path.exists(BASE_DIR / '.env'):
    EMAIL_HOST_USER = config("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
else:
    EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", None)
    EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", None)

django_heroku.settings(locals())

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
