from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = ''

DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS += [
    'debug_toolbar'
]

MIDDLEWARE += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'db.sqlite3'),
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "database_name",
        'USER': "database_user",
        'PASSWORD': "database_password",
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Mailtrap settings
EMAIL_BACKEND= ''
EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = ''


# from .base import *

# # SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = 'django-insecure-e(r*1+g(-39+nc39f&%h9@jd%42zv$q&%dkr+s)$^m!*vwyg_8'

# DEBUG = True

# ALLOWED_HOSTS = []

# # Application definition
# INSTALLED_APPS += []