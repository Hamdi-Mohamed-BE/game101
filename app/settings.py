
import os
import environ
from datetime import timedelta

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
location = lambda x: os.path.join(os.path.dirname(os.path.realpath(__file__)), x)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/
env = environ.Env(DEBUG=(bool, False), ALLOWED_HOSTS=(list, ["*"]))
env.read_env()

IS_DEVELOPMENT = bool(int(os.environ.get("IS_DEVELOPMENT", False)))
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", 'sdfm-bci^u39bw19op25fv@x)*zh7%!q!(@j3r1jez50--sdtd1w2132')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.environ.get("DEBUG", False)))
ALLOWED_HOSTS = [
    'localhost',
]
if DEBUG:
    ALLOWED_HOSTS += ['192.168.{}.{}'.format(i, j) for i in range(256) for j in range(256)]
    ALLOWED_HOSTS += ['127.0.0.1', '0.0.0.0']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',

    'ckeditor',
    'rest_framework',
    'drf_yasg',  # Swagger app
    'core',

    # my apps
    'games',
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
]

CORS_ORIGIN_WHITELIST = [
    'http://127.0.0.1:4200',
    'http://localhost:4200',
    'http://127.0.0.1:8080',
    'http://localhost:8080',
    'http://127.0.0.1:3000',
    'http://localhost:3000',
    'http://34.76.220.67',
]


ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            location('templates')
        ],
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

WSGI_APPLICATION = 'wsgi.application'
X_FRAME_OPTIONS = 'SAMEORIGIN'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'core.pagination.DefaultPager',
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    "EXCEPTION_HANDLER": "core.exception.exception_handler_override",
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=365),
    'ROTATE_REFRESH_TOKENS': True
}

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # this is default
    'guardian.backends.ObjectPermissionBackend',
)

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
if os.environ.get("DATABASE_URL"):
    db = env.db()
    print(env.db(), "DATA_BASE_ACCESS")
else:
    db = {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": os.environ.get("DB_HOST"),
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASS"),
    }

DATABASES = {"default": db}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Prague'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# AUTH_USER_MODEL = 'user.User'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    },
    "DEFAULT_PAGINATOR_INSPECTORS": [
        'drf_yasg.inspectors.CoreAPICompatInspector',
        "core.pagination_swagger.DefaultPagerInspector",
    ],

    'USE_SESSION_AUTH': False,
    # https://github.com/axnsan12/drf-yasg/issues/281
    # Hide models section at the bottom of the swagger view
    'DEFAULT_FIELD_INSPECTORS': [
        'drf_yasg.inspectors.CamelCaseJSONFilter',
        'drf_yasg.inspectors.InlineSerializerInspector',
        'drf_yasg.inspectors.RelatedFieldInspector',
        'drf_yasg.inspectors.ChoiceFieldInspector',
        'drf_yasg.inspectors.FileFieldInspector',
        'drf_yasg.inspectors.DictFieldInspector',
        'drf_yasg.inspectors.JSONFieldInspector',
        'drf_yasg.inspectors.HiddenFieldInspector',
        'drf_yasg.inspectors.RecursiveFieldInspector',
        'drf_yasg.inspectors.SerializerMethodFieldInspector',
        'drf_yasg.inspectors.SimpleFieldInspector',
        'drf_yasg.inspectors.StringDefaultFieldInspector',
    ],
    # 'JSON_EDITOR': True,
}

INCLUDE_HTTPS_SCHEMA = bool(int(os.environ.get("INCLUDE_HTTPS_SCHEMA", True)))

# static files settings
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATIC_ROOT = os.path.join(
    BASE_DIR,'staticfiles'
)

MEDIA_URL = '/upload/images/'
MEDIA_ROOT = os.path.join(BASE_DIR , 'static/upload/images')