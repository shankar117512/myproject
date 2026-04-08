# ─── Builder ─────────────────────────────
FROM python:3.11-slim AS builder

WORKDIR /app

ENV HOME=/tmp \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements/ requirements/
COPY requirements.txt .

RUN pip install --prefix=/install -r requirements.txt

# ─── Runtime ─────────────────────────────
FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /install /usr/local
COPY . .

RUN mkdir -p /app/staticfiles

RUN python manage.py collectstatic --noinput --settings=config.settings.production || true

RUN addgroup --system app && adduser --system --group app
RUN chown -R app:app /app
USER app

CMD ["sh", "-c", "python manage.py migrate --noinput && gunicorn config.wsgi:application --bind 0.0.0.0:$PORT --worker-tmp-dir /dev/shm"]
