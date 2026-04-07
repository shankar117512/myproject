from django.http import JsonResponse
from django.views import View
from django.db import connection
import django


class HealthCheckView(View):
    """Health check endpoint for Railway deployment verification."""

    def get(self, request):
        try:
            # Check database connectivity
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
            db_status = "healthy"
        except Exception as e:
            db_status = f"unhealthy: {str(e)}"

        return JsonResponse(
            {
                "status": "ok" if db_status == "healthy" else "error",
                "database": db_status,
                "django_version": django.get_version(),
                "environment": "operational",
            },
            status=200 if db_status == "healthy" else 503,
        )
