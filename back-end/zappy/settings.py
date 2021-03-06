"""
Django settings for zappy project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$bf$@n@#ixinu6*v-bg(o6qf2u!dqvjo8fc&=71v9t3usv#^o9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['506db91d.ngrok.io','127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'events',
    'rest_framework',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
     'corsheaders.middleware.CorsMiddleware',
     'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'zappy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'zappy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'zappy',
      
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS= (
    os.path.join(BASE_DIR,'static'),
)
STATIC_ROOT=os.path.join(os.path.dirname(BASE_DIR),'static-serve')

# SLACK API Configurations
SLACK_CLIENT_ID = '583322761169.592035565284'
SLACK_CLIENT_SECRET = '63bc864f675cfe45499a9c8f515580d2'
SLACK_VERIFICATION_TOKEN = 'fUyL3DB6u3DDw6eBQUzDbYnr'
SLACK_BOT_USER_TOKEN = 'xoxb-583322761169-589666581664-p7w6i2J3VIqBU366v2kj6K62'
# Tweeter Configrations
CONSUMER_KEY ="W52wVCPOHJoJ5TPLLgsgKAHGr"
CONSUMER_SECRET = "Dhe60CjVGFYd5yEFmnhvoJeUTslGtfmah32HPxIij6UL8FI4Oz"   
ACCESS_KEY = "1111567201952243712-6nRw7xeLBxK5dirvJtNxrsdxyu9uIv"    
ACCESS_SECRET = "mk3nfzuJfU1GnOcX5k9zjBtO33Saj9T6sPeo23FSFbp06"

CORS_ORIGIN_WHITELIST = (
    'http://localhost:4200/',
    'http://localhost:8000/',
)
CORS_ORIGIN_ALLOW_ALL = True
