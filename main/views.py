from django.shortcuts import render
from .models import Tutorial

def index(request):
    tutorials = Tutorial.objects.all()
    context = {
        'tutorials': tutorials
    }
    return render(request, 'index.html', context)
