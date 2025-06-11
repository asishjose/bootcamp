from django.shortcuts import render
#from django.http import HttpResponse
from . models import MovieInfo
from . forms import MovieForm

# Create your views here.

def create(request):
    frm=MovieForm()
    if request.POST:
        # print(request.POST)
        # print(request.POST.get('year'))
        
        # title = request.POST.get('title')
        # year = request.POST.get('year')
        # desc = request.POST.get('description')
        # movie_obj=MovieInfo(title=title, year=year, description=desc)
        # movie_obj.save()

        frm=MovieForm(request.POST)
        if frm.is_valid():
            frm.save()
        else:
            frm=MovieForm()

    return render(request, 'create.html',{'frm':frm})

def list(request):
    movie_set=MovieInfo.objects.all()
    print(movie_set)
    return render(request, 'list.html', {'movies':movie_set })


def edit(request):
    return render(request, 'edit.html')

def home(request):  #  HOME VIEW
    return render(request, 'home.html')