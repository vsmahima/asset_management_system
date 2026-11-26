from django import forms
from .models import AssetRegistration



class AssetRegistrationForm(forms.ModelForm):
    class Meta:
        model = AssetRegistration
       # exclude = ['assetId']
    
        fields = ['asset_name','category','purchase_date','purchase_cost','supplier_name','asset_location','asset_condition','asset_status','asset_description']
        
        widgets = {
            'assetId': forms.TextInput(attrs={
                'readonly': 'readonly',
                'class': 'form-control'
            })
        }