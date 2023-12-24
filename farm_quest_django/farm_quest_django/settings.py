

import os
from pathlib import Path
from urllib import request
import db_settings


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = "django-insecure-)ggi*w1=crxv=#p=%lz@+nh@q0aaz^#6q0x44#v$suouo2dj1a"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'farm_quest_app',
    'users_app',

                    
    # https ssl - kdy
    # 'django_extensions',
    # 'sslserver',

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

ROOT_URLCONF = 'farm_quest_django.urls'



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        # 'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # 로그인 사용자용 user_info 컨텍스트 프로세서 -kdy
                'users_app.user_info.user_info',

            ],
        },
    },
]

WSGI_APPLICATION = 'farm_quest_django.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
    os.path.join(BASE_DIR, 'static') # 경로처리 -kdy
]



# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users_app.User'

LANGUAGE_CODE = 'ko-kr'

LOGIN_REDIRECT_URL = '/'

DATABASES = db_settings.DATABASES
SECRET_KEY = db_settings.SECRET_KEY


# users_app/sign_up2.html 이미지 업로드 기능 관련 -kdy
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# views.py 에서 이메일 발송을 위한 static 경로 설정 -kdy
STATICFILES_DIRS = [ 
    os.path.join(BASE_DIR, 'static')
]

# python manage.py collectstatic 이메일 이미지 첨부 경로를 위한 세팅 -kdy
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# 로그인 사용자 세션 처리 -kdy
# SESSION_ENGINE = "django.contrib.sessions.backends.db"  # 데이터베이스를 세션 저장소로 사용
# SESSION_COOKIE_AGE = 1209600 
# SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"  # 사용자 지정 세션 엔진
# SESSION_COOKIE_AGE = 60 * 60 * 24 * 3  # 3일
# SESSION_EXPIRE_AT_BROWSER_CLOSE = True
# SESSION_COOKIE_SECURE = False
# SESSION_COOKIE_DOMAIN = '127.0.0.1:8000'

