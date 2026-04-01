from .base import *
import os
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from decouple import config

DEBUG = False

ALLOWED_HOSTS = [".railway.app", config("RAILWAY_STATIC_URL", default="*")]

SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"

DATABASES["default"]["OPTIONS"] = {"sslmode": "require"}

SENTRY_DSN = os.getenv("SENTRY_DSN")

if SENTRY_DSN:  # ✅ Only initialize if exists
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        traces_sample_rate=1.0,
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
