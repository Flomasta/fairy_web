from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
    path('create-room/', views.createRoom, name='create_room'),
    path('update-room/<str:pk>/', views.updateRoom, name='update_room'),
    path('delete-room/<str:pk>/', views.deleteRoom, name='delete_room'),
    path('login/', views.loginPage, name='login_page'),
    path('logout/', views.logoutPage, name='logout_page'),
]
