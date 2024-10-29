from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.flatpages import views
from . import views




urlpatterns = [
    
    path("pages/", include("django.contrib.flatpages.urls")),
    path('', views.index, name='home'),
    path('about/', views.about, name='about' ),
    
]

