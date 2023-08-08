from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

rooms = [
    {'id': 1, 'name': 'Lets learn python!'},
    {'id': 2, 'name': 'Lets learn django!'},
    {'id': 3, 'name': 'Lets learn nlp!'},
]


def home(request):
    return render(request, 'base/home.html', {'rooms': rooms})


def room(request, id):
    room = None
    for i in rooms:
        if i['id'] == int(id):
            room = i
    context = {'room': room}
    return render(request, 'base/room.html', context)
