from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from .models import Room, Topic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RoomForm

# Create your views here.


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # try:
        #     User.objects.get(username=username)
        # except:
        #     messages.error(request, 'user doesnot exist')

        # user = authenticate(request, username=username, password=password)

        # if user is not None:
        #     login(request=request, user=user)
        #     return redirect('home')
        # else:
        #     messages.error(request, 'username or password doesnot exist')

    context = {}
    return render(request, "base/login_register.html", context)


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(discription__icontains=q)
    )
    room_count = rooms.count()

    topics = Topic.objects.all()
    return render(request, 'base/home.html', {'rooms': rooms, 'topics': topics, 'room_count': room_count})


def room(request, id):
    room = Room.objects.get(id=id)
    context = {'room': room}
    return render(request, 'base/room.html', context)


@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()
    if (request.method == 'POST'):
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)


@login_required(login_url='login')
def updateRoom(request, id):
    room = Room.objects.get(id=id)
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse("You are not allowed here")

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {'form': form}
    return render(request, 'base/room_form.html', context)


@login_required(login_url='login')
def deleteRoom(request, id):
    room = Room.objects.get(id=id)
    if request.method == 'POST':
        room.delete()
        print("deleted")
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})
