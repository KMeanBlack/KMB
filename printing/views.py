from django.shortcuts import render 
#from django.http import HttpResponse

# Create your views here.
def printing(request):
    return render(request, 'printing/printingsolution.html')

def Trims(request):
    return render(request, 'printing/Trims.html')

def Sustainable(request):
    return render(request, 'printing/sustainable.html')

def Flexible(request):
    return render(request, 'printing/FlexiblePackaging.html')

def Accessories(request):
    return render(request, 'printing/Accessories.html')

def Sustainabletrims(request):
    return render(request, 'printing/sustainabletrims.html')

def Rigidbox(request):
    return render(request, 'printing/Rigidbox.html')