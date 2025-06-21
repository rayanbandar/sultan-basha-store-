SECRET_KEY = 'replace-this-key'
DEBUG = False
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = ['django.contrib.staticfiles', 'store']
ROOT_URLCONF = 'sultan_store.urls'
MIDDLEWARE = ['django.middleware.common.CommonMiddleware']
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': ['store/templates'],
    'APP_DIRS': True,
    'OPTIONS': {'context_processors': []},
}]
STATIC_URL = '/static/'
STATICFILES_DIRS = ['store/static']
