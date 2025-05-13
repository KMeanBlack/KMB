from django.urls import path
from . import views

urlpatterns = [
   path("", views.index, name="index"),
   path("aboutus", views.aboutus, name='aboutus'),
   path("education", views.education, name='studentssection'),   
   path("buyingagent", views.buyingagent, name='buyinghouse'),
   path("printing", views.printing, name='printingsolution'),
   path("products", views.products, name='products'),
   path("services", views.services, name='services'),
   path("contact", views.contact, name='contact'),
   path('signup', views.handleSignUp, name="handleSignUp"),
   path('login', views.handeLogin, name="handleLogin"),
   path('logout', views.handelLogout, name="handleLogout"),
   path('privacy', views.privacy, name="privacy"),
   path('terms', views.terms, name="terms"),
]