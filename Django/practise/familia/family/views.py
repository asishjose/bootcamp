from django.shortcuts import render,redirect
from . models import FamilyMember
from . forms import FamForm
# Create your views here.

def home(request):
    return render(request, 'family/home.html')

def list(request):
    members = FamilyMember.objects.all()
    return render(request, 'family/list.html', {'members':members})

# def create(request):
#     if request.method=='POST':
#         name = request.POST.get('name')
#         age = request.POST.get('age')

#         FamilyMember.objects.create(
#             name=name,
#             age=age
#         )
#         return redirect('list')
#     return render(request, 'family/create.html')

def delete(request, pk):
    instance = FamilyMember.objects.get(pk=pk)
    instance.delete()
    return redirect('list')

# def edit(request,pk):
#     instance = FamilyMember.objects.get(pk=pk)

#     if request.method=='POST':
#         instance.name = request.POST.get('name',instance.name)
#         instance.age = request.POST.get('age',instance.age)
#         instance.save()
#         return redirect('list')

#     return render(request, 'family/edit.html',{'member':instance})

def create(request):
    frm = FamForm()
    if request.method=='POST':
        frm = FamForm(request.POST)
        if frm.is_valid():
            frm.save()
        else:
            frm=FamForm()
    return render(request,'family/create.html',{'frm':frm})

def edit(request,pk):
    edit_instance=FamilyMember.objects.get(pk=pk)
    if request.POST:
        frm=FamForm(request.POST, instance=edit_instance)
        if frm.is_valid():
            edit_instance.save()
    else:
        frm=FamForm(instance=edit_instance)
    frm=FamForm(instance=edit_instance)
    return render(request,'family/create.html',{'frm':frm})