from .base import *
import os
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from decouple import config

DEBUG = False

ALLOWED_HOSTS = ["easygoing-analysis-staging.up.railway.app", "healthcheck.railway.app"]

CSRF_TRUSTED_ORIGINS = ["https://easygoing-analysis-staging.up.railway.app"]

SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"

DATABASES["default"]["OPTIONS"] = {"sslmode": "require"}

SENTRY_DSN = os.getenv("SENTRY_DSN")

if SENTRY_DSN:  # ✅ Only initialize if exists
    sentry_sdk.init(
        dsn="https://bb4d49e6fe255d9b746a6afca468792f@o4511145511944192.ingest.us.sentry.io/4511145515876352",
        traces_sample_rate=1.0,
        send_default_pii=True,
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
