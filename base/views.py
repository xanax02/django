from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

rooms = [
    {'id': 1, 'name': 'Lets learn python!'},
    {'id': 2, 'name': 'Lets learn python!'},
    {'id': 3, 'name': 'Lets learn python!'},
]


def home(request):
    return render(request, 'base/home.html', {'rooms': rooms})


def room(request):
    return render(request, 'base/room.html')
