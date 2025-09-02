from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-b64gm=j2sc6d@y5b@nk97ug%9gr0j)m%h!1!9csr43jjc(4azw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0','192.168.1.2','localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'dashboard',
    'enquiries',
    'approvals',
]

# Add authentication redirects
LOGIN_REDIRECT_URL = 'dashboard:redirect_dashboard'
LOGOUT_REDIRECT_URL = 'accounts:login'

# adsoft/settings.py
AUTH_USER_MODEL = 'accounts.CustomUser'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'adsoft.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'adsoft.wsgi.application'

# Email configuration

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'v.varunprashanth20@gmail.com'
EMAIL_HOST_PASSWORD = 'dtbciuyprqfkkvvt'  # app password without spaces



# Option 2: Use environment variables instead (uncomment to use env-driven config)
# EMAIL_BACKEND = os.getenv('EMAIL_BACKEND', EMAIL_BACKEND)
# EMAIL_HOST = os.getenv('EMAIL_HOST', EMAIL_HOST)
# EMAIL_PORT = int(os.getenv('EMAIL_PORT', EMAIL_PORT))
# EMAIL_USE_TLS = bool(int(os.getenv('EMAIL_USE_TLS', int(EMAIL_USE_TLS))))
# EMAIL_USE_SSL = bool(int(os.getenv('EMAIL_USE_SSL', int(EMAIL_USE_SSL))))
# EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', EMAIL_HOST_USER)
# EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', EMAIL_HOST_PASSWORD)
# DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL', DEFAULT_FROM_EMAIL)
PASSWORD_RESET_TIMEOUT = 60 * 60  # 1 hour in seconds


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'adsoftdb',
        'USER': 'root',
        'PASSWORD': '2005',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
