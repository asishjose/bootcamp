from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

def create(request):
    if request.POST:
        #print(request.POST)
        print(request.POST.get('year'))
    return render(request, 'create.html')

def list(request):
    movie_data = {
        'movies':[ {
        'title':'Godfather',
        'year': 1990,
        'summary':'stroy of an underworld don',
        'success':True,
        'img': 'godfather.jpeg'
    },
    {
        'title':'Goat Life',
        'year': 1990,
        'success':False,
        'img': 'goatlife.jpeg'
    },
    {
        'title':'Empuraan',
        'year': 1990,
        'summary':'stroy of an underworld don',
        'success':False,
        'img': 'empuran.jpeg'
    }
        ]}
    return render(request, 'list.html', movie_data)


def edit(request):
    return render(request, 'edit.html')

def home(request):  #  HOME VIEW
    return render(request, 'home.html')