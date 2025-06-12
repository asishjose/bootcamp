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


def edit(request,pk):
    instance_to_be_edited=MovieInfo.objects.get(pk=pk)
    if request.POST:
        # title=request.POST.get('title')
        # year=request.POST.get('year')
        # description=request.POST.get('description')
        # instance_to_be_edited.title=title
        # instance_to_be_edited.year=year
        # instance_to_be_edited.description=description
        # instance_to_be_edited.save()
        frm=MovieForm(request.POST, instance=instance_to_be_edited)
        if frm.is_valid():
            instance_to_be_edited.save()
    else:
        frm=MovieForm(instance=instance_to_be_edited)
        
    frm=MovieForm(instance=instance_to_be_edited)
    return render(request, 'create.html',{'frm':frm})

def home(request):  #  HOME VIEW
    return render(request, 'home.html')

def delete(request,pk):
    instance=MovieInfo.objects.get(pk=pk)
    instance.delete()
    movie_set=MovieInfo.objects.all()
    return render(request, 'list.html', {'movies':movie_set })
