from django.shortcuts import render,redirect
from . models import FamilyMember
# Create your views here.

def home(request):
    return render(request, 'family/home.html')

def list(request):
    members = FamilyMember.objects.all()
    return render(request, 'family/list.html', {'members':members})

def create(request):
    if request.method=='POST':
        name = request.POST.get('name')
        age = request.POST.get('age')

        FamilyMember.objects.create(
            name=name,
            age=age
        )
        return redirect('list')
    return render(request, 'family/create.html')

def delete(request, pk):
    instance = FamilyMember.objects.get(pk=pk)
    instance.delete()
    return redirect('list')

def edit(request,pk):
    instance = FamilyMember.objects.get(pk=pk)

    if request.method=='POST':
        instance.name = request.POST.get('name',instance.name)
        instance.age = request.POST.get('age',instance.age)
        instance.save()
        return redirect('list')

    return render(request, 'family/edit.html',{'member':instance})