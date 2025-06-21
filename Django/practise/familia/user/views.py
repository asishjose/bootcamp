from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def notworking(request):
    if request.method == 'GET':
        return HttpResponse('The page is not working')