from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("aboutus/", views.aboutus, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),

    #Errors page
    path("404",views.Error404, name='404'),
    path("faq",views.faq, name='faq'),

    #account urls
    path('account/my-account',views.MY_ACCOUNT, name='my_account'),
    path('account/register', views.REGISTER, name='handleregister'),
    path('account/login', views.LOGIN, name='handlelogin'),
    path('account/profile',views.PROFILE,name='profile'),
    path('account/profile/update',views.PROFILE_UPDATE,name="profile_update"),
    path('accounts/', include('django.contrib.auth.urls')),

]
