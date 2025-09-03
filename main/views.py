from django.shortcuts import render

def index(request):
    context = {
        'name': 'красавчик',
    }
    return render(request, 'index.html', context)
