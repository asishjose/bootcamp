from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('list/',views.list, name='list'),
    path('create/',views.create, name='create'),
    path('update/',views)
]
