from django.urls import path
from . import views

urlpatterns = [
    path("",views.login,name="login"),
    path("index/",views.index,name="index"),
    path("asset_registration/",views.asset_registration,name="asset_registration"),
    path("asset_allocation/",views.asset_allocation,name="asset_allocation"),
    path("maintenence/",views.maintenence,name="maintenence"),
    path("reports/",views.reports,name="reports"),
    
]
