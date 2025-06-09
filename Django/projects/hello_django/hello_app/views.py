from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def print_hello(request):
    movie_data = {
        'movies':[ {
        'title':'Godfather',
        'year': 1990,
        'summary':'stroy of an underworld don',
        'success':True
    },
    {
        'title':'Goat Life',
        'year': 1990,
        'success':False
    },
    {
        'title':'Empuraan',
        'year': 1990,
        'summary':'stroy of an underworld don',
        'success':False
    }
        ]}
    return render(request, 'hello.html', movie_data)
def home(request):  # NEW VIEW
    return HttpResponse("Welcome to Django! Go to /hello/ to see the hello message.")