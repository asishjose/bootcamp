from django.urls import path
from . import views

urlpatterns=[
    path('home/', views.home,name='create'),
    path('',views.homee),
    path('create/', views.create, name='create'),
    path('list/', views.list, name='list')
]