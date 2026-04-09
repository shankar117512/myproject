from django.http import HttpResponse
from django.http import JsonResponse
from django.db import connections
from django.db.utils import OperationalError


def home(request):
    return HttpResponse("Django Production Deployed Was Successfully...! 🚀")


def health_check(request):
    db_status = "healthy"

    try:
        # Try connecting to the database
        connections["default"].cursor()
    except OperationalError:
        db_status = "unhealthy"

    return JsonResponse({"status": "ok", "database": db_status})


def trigger_error(request):
    division_by_zero = 1 / 0
