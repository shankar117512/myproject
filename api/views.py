from django.http import HttpResponse


def home(request):
    return HttpResponse("Django Production Deployed Was Successfully...!")
