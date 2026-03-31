import sentry_sdk
from decouple import config
from sentry_sdk.integrations.django import DjangoIntegration

from .base import DATABASES

DEBUG = False

ALLOWED_HOSTS = [".railway.app", config("RAILWAY_STATIC_URL", default="*")]

SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"

DATABASES["default"]["OPTIONS"] = {"sslmode": "require"}

SENTRY_DSN = config("SENTRY_DSN", default="")
if SENTRY_DSN:
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=[DjangoIntegration()],
        environment="staging",
        traces_sample_rate=0.5,
    )

CORS_ALLOWED_ORIGINS = config(
    "CORS_ALLOWED_ORIGINS",
    default="https://staging.yourdomain.com",
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
        "level": "INFO",
    },
}
