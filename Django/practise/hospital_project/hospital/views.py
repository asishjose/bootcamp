from django.shortcuts import render

# Create your views here.
from . models import Doctor,Patient

def home(request):
    return render(request,'hospital/home.html')

def doctor_list(request):
    doctors=Doctor.objects.all()
    return render(request, 'hospital/doctor_list.html', {'doctors':doctors})

def patient_list(request):
    patients=Patient.objects.all()
    return render(request, 'hospital/patient_list.html',{'patients':patients})