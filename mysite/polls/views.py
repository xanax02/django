from django.http import HttpResponse;

def index(request):
    return HttpResponse("Hello World, you are at poll index");