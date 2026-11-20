from django import forms
from .models import AssetRegistration



class AssetRegistrationForm(forms.ModelForm):
    class Meta:
        model = AssetRegistration
        fields = "__all__"