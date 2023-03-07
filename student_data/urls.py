from django.urls import path
from . import views

urlpatterns = [path('query_set', views.query_set, name='query_set'),
               path('student_info', views.student_info, name='student_info')]

