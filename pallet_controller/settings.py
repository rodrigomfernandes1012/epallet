# No settings.py - CONFIGURAÇÃO TEMPORÁRIA PARA DEBUG
import os
from pathlib import Path
import dj_database_url
from pathlib import Path

BASE_DIR = Path(__file__ ).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-6c!7%^w=v&0++twoi_5d0g5jdy5xvr)35v#dqn7wp#u%j6^3i#')
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

# PERMITIR TODOS OS HOSTS TEMPORARIAMENTE
ALLOWED_HOSTS = ['*']

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

# BANCO DE DADOS - CONECTA AO SUPABASE EXISTENTE (NÃO ALTERA DADOS)
DATABASE_URL = os.environ.get('DATABASE_URL')
if DATABASE_URL:
    DATABASES = {
        'default': dj_database_url.config(
            default=DATABASE_URL,
            conn_max_age=600,
            ssl_require=True
        )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'postgres',
            'PASSWORD': '5IEvXIKjw9BN2QOx',
            'HOST': 'db.zyeaqpsltgavouygatxs.supabase.co',
            'PORT': '5432',
            'OPTIONS': {
                'sslmode': 'require',
            },
        }
    }

# Resto das configurações...
AUTH_USER_MODEL = 'app_controller.Usuario'
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'painel_usuario'
LOGOUT_REDIRECT_URL = 'login'

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SUPABASE_URL = os.environ.get('SUPABASE_URL', 'https://zyeaqpsltgavouygatxs.supabase.co' )
SUPABASE_KEY = os.environ.get('SUPABASE_KEY', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inp5ZWFxcHNsdGdhdm91eWdhdHhzIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDc4MjQ4NDMsImV4cCI6MjA2MzQwMDg0M30.L9SVkjKQk2cVygHIIcjC0T9YQ_SEZXRUvSSMOYhDWvE')

# Static files - CONFIGURAÇÃO CORRIGIDA
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Criar diretório se não existir
if not os.path.exists(STATIC_ROOT):
    os.makedirs(STATIC_ROOT, exist_ok=True)

# Diretórios de arquivos estáticos durante desenvolvimento
STATICFILES_DIRS = []
static_dev_dir = os.path.join(BASE_DIR, 'static')
if os.path.exists(static_dev_dir):
    STATICFILES_DIRS.append(static_dev_dir)

# WhiteNoise configuration
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
