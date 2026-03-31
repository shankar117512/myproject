import sys, os

sys.path.insert(
    0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)

from config.settings.base import *

DEBUG = True

ALLOWED_HOSTS = [
    "easygoing-analysis-dev.up.railway.app",
    "localhost",
    "127.0.0.1",
]

CSRF_TRUSTED_ORIGINS = ["https://easygoing-analysis-dev.up.railway.app"]

INSTALLED_APPS += [  # noqa: F405
    "debug_toolbar",
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",  # noqa: F405
]

INTERNAL_IPS = ["127.0.0.1"]

DATABASES  # noqa: F405 ["default"]["OPTIONS"] = {"sslmode": "disable"}

CORS_ALLOW_ALL_ORIGINS = True

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {"class": "logging.StreamHandler"},
    },
    "root": {
        "handlers": ["console"],
        "level": "DEBUG",
    },
}
