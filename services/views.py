from django.shortcuts import render 
#from django.http import HttpResponse

# Create your views here.
def services(request):
    return render(request, 'services/services.html')

def graphicdesign(request):
    return render(request, 'services/graphic.html')

def websites(request):
    return render(request, 'services/website.html')

def detail(request):
    return render(request, 'services/websitepage/detail.html')

def webdesigning(request):
    return render(request, 'services/websitepage/webdesigning.html')

def webdevelop(request):
    return render(request, 'services/websitepage/webdevelop.html')

def Iosapps(request):
    return render(request, 'services/websitepage/Iosapps.html')