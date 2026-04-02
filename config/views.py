from django.http import HttpResponse
from django.http import JsonResponse


def home(request):
    return HttpResponse("Django staging deployed successfully...! 🚀")


def health_check(request):
    return JsonResponse({"status": "ok"})
