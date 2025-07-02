import os
from pathlib import Path
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in product

# Configurações do Supabase
SUPABASE_URL = 'https://zyeaqpsltgavouygatxs.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inp5ZWFxcHNsdGdhdm91eWdhdHhzIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDc4MjQ4NDMsImV4cCI6MjA2MzQwMDg0M30.L9SVkjKQk2cVygHIIcjC0T9YQ_SEZXRUvSSMOYhDWvE'
#SECRET_KEY = 'django-insecure-6c!7%^w=v&0++twoi_5d0g5jdy5xvr)35v#dqn7wp#u%j6^3i#'

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-uma-chave-local-para-desenvolvimento')
#teste

# O valor 'False' é o padrão se a variável RENDER não estiver definida
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'False'

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True


#ALLOWED_HOSTS = ['ponto.nfiscal.com.br', 'localhost']


ALLOWED_HOSTS = []

# Lógica para adicionar o domínio do Heroku dinamicamente
# O Heroku define a variável 'DYNO' no ambiente de execução.
# Podemos usá-la para saber que estamos em produção.
if 'DYNO' in os.environ:
    # Adiciona o domínio principal do Heroku e o www (boa prática)
    ALLOWED_HOSTS.append('epallet-41b825a7d788.herokuapp.com')
    ALLOWED_HOSTS.append('www.epallet-41b825a7d788.herokuapp.com')

# Para desenvolvimento local, você pode adicionar o host local
# Apenas se DEBUG for True
if os.environ.get('DEBUG', 'False').lower() == 'true':
    ALLOWED_HOSTS.append('127.0.0.1')


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
    'whitenoise.middleware.WhiteNoiseMiddleware', # Adicione esta linha
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


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases



#Realizar demanda de backend- Utilizar SupaBase como teste.
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': 'postgres',
#        'USER': 'postgres',
#        'PASSWORD': '5IEvXIKjw9BN2QOx',
#        'HOST': 'db.zyeaqpsltgavouygatxs.supabase.co',
#        'PORT': '5432',
#    }
#}

# Adicione esta configuração dinâmica
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600,
        ssl_require=True # Essencial para o Postgres do Heroku
    )
}



AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]
# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'painel_usuario'
AUTH_USER_MODEL = 'app_controller.Usuario'


LANGUAGE_CODE = 'en-us'


TIME_ZONE = 'America/Sao_Paulo'  # Fuso horário de Brasília


USE_I18N = True

USE_TZ = True

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  # Para desenvolvimento
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')    # Para produção
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field


# Configuração do WhiteNoise para armazenamento
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --------------------------------------------------------------------------
# CONFIGURAÇÕES DE AUTENTICAÇÃO E REDIRECIONAMENTO
# --------------------------------------------------------------------------

# Para onde o usuário vai após um login bem-sucedido.
# Use o NOME da sua rota de dashboard ou página principal.
# Se sua página principal é a raiz, '/' é uma opção segura.
# Se você tem uma rota como path('dashboard/', views.dash, name='dashboard'),
# use 'dashboard'. Vamos começar com '/'.
LOGIN_REDIRECT_URL = '/clientes'

# Para onde o usuário vai após fazer logout.
# Geralmente, é a página de login ou a página inicial.
LOGIN_URL = '/logout' # A página que contém seu formulário de login

# Para onde o usuário vai após um logout bem-sucedido.
LOGOUT_REDIRECT_URL = '/logout'


