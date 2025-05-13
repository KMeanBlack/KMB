from django.urls import path
from . import views

urlpatterns = [
    path("", views.printing, name='Printing section'),
    path("trims", views.Trims, name='Trims'),
    path("sustainable", views.Sustainable, name='Sustainable'),
    path("flexible", views.Flexible, name='Flexible'),
    path("accessories", views.Accessories, name='Accessories'),
    path("sustainabletrims", views.Sustainabletrims, name='Sustainabletrims'),
    path("rigidbox", views.Rigidbox, name='Rigidbox')
    ]