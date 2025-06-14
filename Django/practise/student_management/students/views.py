from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import StudentInfo

# Create your views here.
def home(request):
    return HttpResponse('This is Home Page')

def list(request):
    students_details = StudentInfo.objects.all()
    return render(request, 'list.html', {'StudentInfo':students_details})

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        year = request.POST.get('year')
        address = request.POST.get('address')

        StudentInfo.objects.create(name=name, year=year, address=address)
        return redirect('list')
    return render(request,'create.html')