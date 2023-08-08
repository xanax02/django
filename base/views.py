from django.shortcuts import render
from .models import Room

# Create your views here.


def home(request):
    rooms = Room.objects.all()
    return render(request, 'base/home.html', {'rooms': rooms})


def room(request, id):
    room = None
    for i in rooms:
        if i['id'] == int(id):
            room = i
    context = {'room': room}
    return render(request, 'base/room.html', context)
