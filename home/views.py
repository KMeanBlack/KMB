from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout

#from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'home/home.html')

def aboutus(request):
    #return HttpResponse("this is about us page")
    return render(request, 'home/aboutus.html')

def education(request):
    #return HttpResponse("this is services page")
    return render(request, 'education/index.html')

def buyingagent(request):
    #return HttpResponse("this is contact page")
    return render(request, 'buyingagent/buyingagent.html')

def printing(request):
    #return HttpResponse("this is product page")
    return render(request, 'printing/printingsolution.html')

def products(request):
    #return HttpResponse("this is product page")
    return render(request, 'products/products.html')

def services(request):
    #return HttpResponse("this is product page")
    return render(request, 'services/services.html')

def privacy(request):
    #return HttpResponse("this is product page")
    return render(request, 'home/privacy.html')

def terms(request):
    #return HttpResponse("this is product page")
    return render(request, 'home/terms.html')

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        company_name=request.POST['company_name']
        content =request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, email=email, phone=phone, company_name=company_name, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, "home/contact.html")

def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        if len(username)<10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('index')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('index')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('index')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your iCoder has been successfully created")
        return redirect('index')

    else:
        return HttpResponse("404 - Not found")   
        
def hanldeLogout(request):
    return HttpResponse("index")


def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("index")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("index")

    return HttpResponse("404- Not found")
    return HttpResponse("login")

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('index')

