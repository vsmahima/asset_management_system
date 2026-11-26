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

    last_asset = AssetRegistration.objects.filter(assetId__startswith="AST").order_by('-assetId').first()

    if last_asset:
        last_number = int(last_asset.assetId.replace("AST", ""))
        next_number = last_number + 1
    else:
        next_number = 1

    next_asset_id = f"AST{next_number:03d}"

    if request.method == "POST":
        form = AssetRegistrationForm(request.POST)
        if form.is_valid():
            asset = form.save(commit=False)

            asset.assetId = next_asset_id
            asset.save()
            return redirect('asset_registration')
            #print("data saved successfully")
    else:
            
        form = AssetRegistrationForm(initial={
            'assetId': next_asset_id})
 
    return render(request,"asset_registration.html",{"form":form})

################################################
def asset_allocation(request):
    return render(request,"asset_allocation.html")
def maintenence(request):
    return render(request,"maintenence.html")
def reports(request):
    return render(request,"reports.html")
