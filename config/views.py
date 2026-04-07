from django.http import HttpResponse
from django.http import JsonResponse


def home(request):
    return HttpResponse("Django Production Was Deployed Successfully...! 🚀")


def health_check(request):
    return JsonResponse({"status": "ok"})


def trigger_error(request):
    division_by_zero = 1 / 0
