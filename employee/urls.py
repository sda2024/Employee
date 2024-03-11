from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('create/createEmployee/', views.createEmployee),
    path('delete/<int:id>', views.delete, name='delete'),
]