from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('set/', views.setcookie, name='set'),
    path('get/', views.getcookie, name='get'),
    path('del/', views.delcookie, name='del'),
    path('sessiondemo/', views.my_other_view, name='sessiondemo'),
    path('deletesession/', views.my_third_view, name='deletesession')
  ]
