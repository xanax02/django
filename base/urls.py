from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('', views.home, name="home"),
    path('room/<slug:id>', views.room, name="room"),
    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<slug:id>', views.updateRoom, name='update-room'),
    path('delete-room/<slug:id>', views.deleteRoom, name='delete-room')

]
