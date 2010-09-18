# Django settings for community project.
# ALL YOUR BASES ARE BELONG TO ME

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'mysql'     # 'postgresql', 'mysql', 'sqlite3' or 'ado_mssql'.
DATABASE_NAME = 'tictactoe'           # Or path to database file if using sqlite3.
DATABASE_USER = 'root'             # Not used with sqlite3.
DATABASE_PASSWORD = 'password'     # Not used with sqlite3.
DATABASE_HOST = ''  # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = '3306'             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. All choices can be found here:
# http://www.postgresql.org/docs/current/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
#TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/data/media/'
# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"

MEDIA_URL = '/'

#EDITOR_EMAIL = ''


ADMIN_ID=1

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/adminmedia/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '#huu88qg&h(_2qbv=^rl=9@z7%=@@m%^$4f6q(etds1spz3ae_'


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#    'django.core.context_processors.request',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
#    'globalatlanta.middleware.mobile_redirect.MobileRedirect',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
)

ROOT_URLCONF = 'tic_tac_toe.urls'

TEMPLATE_DIRS = (
    "C:/data/tictactoe/tic_tac_toe/templates", 
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.comments',
    'django.contrib.humanize',
    
    'tic_tac_toe.board',
)

#The directory for user uploaded files

ABS_URL="/"
UPLOAD_DIR = 'upload/'

COOKIE_DOMAIN=""
SESSION_COOKIE_DOMAIN = ''
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# SUPERFILE FIELD SETTINGS
IMG_MODE=2
IMG_QUALITY=75
IMG_WIDTH=300
IMG_HEIGHT=225

#WEATHER_PARTNER='statesboro'
#WEATHER_ZIP='30458'

#EMAIL_HOST='smtp.globalatlanta.com'
#EMAIL_PORT='25'
#EMAIL_HOST_USER = 'admin@globalatlanta.com'
#EMAIL_HOST_PASSWORD = 'globalatlanta'
#
#RECAPTCHA_PUB_KEY = "6Lc4jbwSAAAAAFiwvbt6B28dOsB7Ff8cj06tNGJ3 "
#RECAPTCHA_PRIVATE_KEY = "6Lc4jbwSAAAAAM523d3I4NofQTLFlmcKOMXwzCiP"


#EFROM='noreply@gmail.com'
#EMAIL_USE_TLS = ""

#NUM_ARTICLES_FRONTPAGE=7
#
#REQUIRE_EVENT_APPROVAL=True

