from django.urls import path
from . import views

urlpatterns = [
    path("", views.services, name='services'),
    path("graphicdesign", views.graphicdesign, name='Graphic design'),
    path("websites", views.websites, name='Websites'),
    path("detail", views.detail, name='Detail'),
    path("webdesigning", views.webdesigning, name='webdesigning'),
    path("webdevelop", views.webdevelop, name='webdevelop'),
    path("Iosapps", views.Iosapps, name='Iosapps'),
    ]