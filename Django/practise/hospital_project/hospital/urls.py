from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('doctors/,',views.doctor_list,name='doctor_list'),
    path('',views.patient_list,name='patient_list'),
]