from django.urls import path
from . import views

urlpatterns = [path('registration', views.registration, name='registration'),
               path('register', views.register, name='register'),
               path('login', views.login, name='login'),
               path('logout', views.logout, name='logout')
               ]
