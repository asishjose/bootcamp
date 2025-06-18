from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('list/',views.list, name='list'),
    path('create/', views.create, name='create'),
    path('delete/<pk>', views.delete, name='delete'),
    path('edit/<pk>', views.edit, name='edit'),

]
