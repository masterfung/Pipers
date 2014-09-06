"""
Django settings for piper project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SITE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nb*#c7du)d%38(gze69^f_+kn1i)u=7=&gr+73z(fpf_*)w@)7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'piper.urls'

WSGI_APPLICATION = 'piper.wsgi.application'

SOCIAL_AUTH_TWITTER_LOGIN_URL = "profile"
SOCIAL_AUTH_LOGIN_URL = "profile"
LOGIN_URL = "/login/"

SOCIAL_AUTH_TWITTER_KEY = 'VMc8w90FdAsy5JX5APry9b6DV'
SOCIAL_AUTH_TWITTER_SECRET = 'pqfGMXoYQP5ERgGlGkVy1XBiQQ0l68g7F92NBlz9cxGmknzmzn'

SOCIAL_AUTH_AUTHENTICATION_BACKENDS = (
    'social.backends.open_id.OpenIdAuth',
    'social.backends.twitter.TwitterOAuth',
)


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'piper',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, "templates"),
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static", "static"),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'media')