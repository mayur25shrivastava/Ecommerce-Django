from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="ShoppHooome"),
    path('about/', views.about, name="Aboutt Uss"),
    path('contact/', views.contact, name="contact"),
    path('tracker/', views.tracker, name="Tracking Statusss"),
    path('search/', views.search, name="search"),
    path('products/<int:myid>', views.productview, name="Product view"),
    path('checkout/', views.checkout, name="ckeckout"),
    # path('handlerequest/', views.handlerequest, name="HandleRequest"),
]