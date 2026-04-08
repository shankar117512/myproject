from django.views import View
from django.http import JsonResponse
from django.db import connection
import django


class HealthCheckView(View):
    """Health check endpoint for Railway deployment verification."""

    def get(self, request):
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
            db_status = "healthy"
            status_code = 200
        except Exception:
            db_status = "unavailable"
            status_code = 200  # Always return 200 for health checks

        return JsonResponse(
            {
                "status": "ok",
                "database": db_status,
                "django_version": django.get_version(),
            },
            status=status_code,
        )
