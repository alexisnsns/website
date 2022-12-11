from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def life(request):
    return render(request, 'life.html', {})

def videos(request):
    return render(request, 'videos.html', {})
