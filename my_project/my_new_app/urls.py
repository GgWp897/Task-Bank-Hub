from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('auth/', views.auth, name='auth'),
    path('registration/', views.registration, name='registration'),
    path('home/', views.home, name='home'),
    path('logout/', views.logoutxz, name='logoutxz'),
    path('admin/', views.admin, name='admin'),
    path('', views.welcome, name='welcome')
]
