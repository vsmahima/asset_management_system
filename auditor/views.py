from django.shortcuts import render,redirect
from .models import AssetRegistration
from .forms import AssetRegistrationForm



# Create your views here.

#####LOGIN SESSION######

def login(request):
    uname="mahima"
    pswd="mahima123"
    msg=""
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        if(username == uname and password == pswd):
            return redirect("index")
        else:
            msg = "Invalid Username/Password"
        
    return render(request,"login.html",{'msg':msg})
#######################################################

def index(request):
    return render(request,"index.html")


#######NEW ASSET REGISTRATION ###############

def asset_registration(request):
    if request.method == "POST":
        form = AssetRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("data saved successfully")
        else:
            print(form.errors)
    else:
        form =AssetRegistrationForm()
    return render(request,"asset_registration.html",{"form":form})

################################################
def asset_allocation(request):
    return render(request,"asset_allocation.html")
def maintenence(request):
    return render(request,"maintenence.html")
def reports(request):
    return render(request,"reports.html")
