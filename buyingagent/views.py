from django.shortcuts import render 
#from django.http import HttpResponse

# Create your views here.
def buyingagent(request):
    return render(request, 'buyinghouse/buyingagent.html')