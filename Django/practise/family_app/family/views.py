from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import FamilyMember

# Create your views here.

# def home(request):
#     return HttpResponse('Here is the Home Page for Family App..❤️')

def home(request):
    return render(request, 'family/home.html')

def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        housename = request.POST.get('housename')
        contact = request.POST.get('contact')

        FamilyMember.objects.create(
            name=name,
            age=age,
            housename=housename,
            contact=contact
        )
        return redirect('list')
    return render(request, 'family/add.html')

def list(request):
    members = FamilyMember.objects.all()
    return render(request, 'family/list.html', {'members':members})

def edit_list(request):
    members = FamilyMember.objects.all()
    return render(request, 'family/edit_list.html', {'members': members})


def update(request, pk):
    instance = FamilyMember.objects.get(pk=pk)
    
    if request.method == 'POST':
        instance.name = request.POST.get('name', instance.name)
        instance.age = request.POST.get('age', instance.age)
        instance.housename = request.POST.get('housename', instance.housename)
        instance.contact = request.POST.get('contact', instance.contact)
        instance.save()
        return redirect('list')
    
    return render(request, 'family/edit.html', {'member': instance})

def delete(request,pk):
    instance = FamilyMember.objects.get(pk=pk)
    instance.delete()
    return redirect('edit_list')