from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import MovieInfo

#from . models import MovieInfo
#from . forms import MovieForm
# Create your views here.


def homee(request):
    return HttpResponse('Home Page of Movie Manager')

def home(request):
    return render(request,'home.html')

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        year = request.POST.get('year')

        MovieInfo.objects.create(title=title, year=year)
        return redirect('create')
    movies = MovieInfo.objects.all()
    return render(request,'create.html',{'MovieInfo':movies})

def list(request):
    movies = MovieInfo.objects.all()
    return render(request, 'list.html',{'MovieInfo':movies})