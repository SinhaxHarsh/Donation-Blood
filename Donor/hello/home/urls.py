from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name="home"),
    path('registeration',views.registeration,name="register"),
    path('dashboard',views.dashboard,name="dashboard"),
]
