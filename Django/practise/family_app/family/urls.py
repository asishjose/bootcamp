from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('list/', views.list, name='list'),
    path('edit_list/', views.edit_list, name='edit_list'),
    path('edit/<pk>', views.update, name='edit'),
    path('delete/<pk>', views.delete, name='delete'),
]
