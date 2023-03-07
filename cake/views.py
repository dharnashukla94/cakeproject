from django.shortcuts import render
from .models import DataDescription

# Create your views here.

def index(request):
    dests = DataDescription.objects.all()
    return render(request, 'index.html', {'d1': dests})

