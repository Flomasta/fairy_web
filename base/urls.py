from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
    path('create-room/', views.createRoom, name='create_room'),
    path('update-room/<str:pk>/', views.updateRoom, name='update_room'),
    path('delete-room/<str:pk>/', views.deleteRoom, name='delete_room'),
    path('login/', views.loginPage, name='login_page'),
    path('logout/', views.logoutPage, name='logout_page'),
    path('register/', views.registerPage, name='register_page'),
    path('delete-message/<str:pk>/', views.deleteMessage, name='delete_message'),
    path('profile/<str:pk>/', views.userProfile, name='user-profile'),
    path('update-user/', views.updateUser, name='update-user'),
    path('topics/', views.topicsPage, name='topics'),
    path('activity/', views.activityPage, name='activity'),
    path('api/', include('base.api.urls')),

]
