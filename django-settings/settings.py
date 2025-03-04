INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'authentication',
]

AUTH_USER_MODEL = 'authentication.CustomUser'

# this is for CONSOLE USE
EMAIL_CONSOLE = 'django.core.mail.backends.console.EmailBackend'