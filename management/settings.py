import os
from pathlib import Path
import environ

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Use environ for environment variables
env = environ.Env()
environ.Env.read_env()  # Read environment variables from a .env file

# Media settings
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Security settings
SECRET_KEY = env('SECRET_KEY', default='django-insecure-b9gyuvf3d6qeyeke2#0b^x=!y3z@dng9(kdig=$ceo&1g@in%$')
DEBUG = env.bool('DEBUG', default=True)
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'])

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cafe',  # Your app
]

# Middleware settings
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL configuration
ROOT_URLCONF = 'management.urls'

# Templates configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Add this line
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

# WSGI application
WSGI_APPLICATION = 'management.wsgi.application'

# Database settings (SQLite for dev)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation settings
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

# Localization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files settings
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Default auto field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Session settings
SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Store sessions in the DB
SESSION_COOKIE_AGE = 3600  # 1 hour, adjust as needed
SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # Keep session active even after the browser is closed
SESSION_SAVE_EVERY_REQUEST = True  # Save session on each request

# Stripe API keys (Using environ for production environments)
STRIPE_TEST_SECRET_KEY = env('STRIPE_TEST_SECRET_KEY', default='sk_test_51RDle1Crf6KByO5UQ41lRC8CsWBtjDkiTcdpW2hWnKnoNo9ZZMWQxtneOVxY2A8ZulsLKNfLs3TPf7NspE1Vwpb300YH4gY4fT')
STRIPE_TEST_PUBLIC_KEY = env('STRIPE_TEST_PUBLIC_KEY', default='pk_test_51RDle1Crf6KByO5UHtn0g9u8mA8z7kwB8lmlVe8QLWlF1DGm82OshsJmhWo5S0dUyqC1ifoapUpINGbveCM1gUdd00Wbvh801T')

# Add your other settings below (like logging, email, etc.)