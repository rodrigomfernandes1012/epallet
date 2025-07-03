import os
from pathlib import Path
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-uma-chave-local-para-desenvolvimento')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

# Configuração de hosts permitidos
ALLOWED_HOSTS = []

# Lógica para adicionar o domínio do Heroku dinamicamente
if 'DYNO' in os.environ:
    # Adiciona o domínio principal do Heroku
    ALLOWED_HOSTS.append('epallet-41b825a7d788.herokuapp.com')
    ALLOWED_HOSTS.append('www.epallet-41b825a7d788.herokuapp.com')

# Para desenvolvimento local
if DEBUG:
    ALLOWED_HOSTS.extend(['127.0.0.1', 'localhost'])

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_controller',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pallet_controller.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'pallet_controller.wsgi.application'

# ============================================================================
# CONFIGURAÇÃO DO BANCO DE DADOS - SUPABASE
# ============================================================================

# Configuração para usar Supabase em produção e desenvolvimento
if 'DYNO' in os.environ:
    # PRODUÇÃO: Usar Supabase via variável de ambiente DATABASE_URL
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ.get('DATABASE_URL'),
            conn_max_age=600,
            ssl_require=True  # Essencial para conexões externas
        )
    }
else:
    # DESENVOLVIMENTO: Configuração direta do Supabase
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'postgres',
            'PASSWORD': '5IEvXIKjw9BN2QOx',  # Substitua pela sua senha real
            'HOST': 'db.zyeaqpsltgavouygatxs.supabase.co',
            'PORT': '5432',
            'OPTIONS': {
                'sslmode': 'require',  # Importante para Supabase
            },
        }
    }

# Authentication backends
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

# Password validation
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

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

# Configurações de autenticação e redirecionamento
AUTH_USER_MODEL = 'app_controller.Usuario'
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'painel_usuario'
LOGOUT_REDIRECT_URL = 'login'

# Internationalization
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# WhiteNoise configuration
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ============================================================================
# CONFIGURAÇÕES DO SUPABASE
# ============================================================================

# Configurações do Supabase para uso nas views/APIs
SUPABASE_URL = os.environ.get('SUPABASE_URL', 'https://zyeaqpsltgavouygatxs.supabase.co')
SUPABASE_KEY = os.environ.get('SUPABASE_KEY', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inp5ZWFxcHNsdGdhdm91eWdhdHhzIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDc4MjQ4NDMsImV4cCI6MjA2MzQwMDg0M30.L9SVkjKQk2cVygHIIcjC0T9YQ_SEZXRUvSSMOYhDWvE')

# Configurações de logging para debug
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
    },
    'loggers': {
        'django.db.backends': {
            'level': 'DEBUG' if DEBUG else 'INFO',
            'handlers': ['console'],
        },
    },
}

