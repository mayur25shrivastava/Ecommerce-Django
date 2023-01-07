#this is not prrebuild we make this

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="bloggHooome"),
]