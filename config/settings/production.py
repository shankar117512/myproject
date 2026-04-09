from .base import *
import os
import dj_database_url
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from decouple import config

DEBUG = False

ALLOWED_HOSTS = ["stellar-wholeness-production1.up.railway.app"]

CSRF_TRUSTED_ORIGINS = ["https://stellar-wholeness-production1.up.railway.app"]

# Static files fix for Railway
WHITENOISE_USE_FINDERS = True

SECURE_BROWSER_XSS_FILTER = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = "DENY"
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

DATABASES = {
    "default": dj_database_url.parse(
        config("DATABASE_URL").strip(), conn_max_age=600, ssl_require=False
    )
}

SENTRY_DSN = config("SENTRY_DSN", default="")
if SENTRY_DSN:
    sentry_sdk.init(
        dsn="https://bb4d49e6fe255d9b746a6afca468792f@o4511145511944192.ingest.us.sentry.io/4511145515876352",
        integrations=[DjangoIntegration()],
        environment="production",
        traces_sample_rate=0.1,
    )

CORS_ALLOWED_ORIGINS = config(
    "CORS_ALLOWED_ORIGINS",
    default="https://yourdomain.com",
    cast=lambda v: [s.strip() for s in v.split(",")],
)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {"class": "logging.StreamHandler"},
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
}
