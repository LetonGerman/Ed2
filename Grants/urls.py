from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addgrant/', views.addgrant, name='addgrant'),
    path('insert/', views.insert, name='insert')
]