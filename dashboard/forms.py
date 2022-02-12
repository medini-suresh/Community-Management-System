from django import forms
from accounts.models import Owner, Tenant

from society.models import Flat, Society

class FlatForm(forms.ModelForm):
    class Meta:
        model = Flat
        exclude = ['created_at', 'updated_at']
    
class SocietyForm(forms.ModelForm):
    class Meta:
        model = Society
        exclude = ['created_at', 'updated_at']
    
class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        exclude = ['created_at', 'updated_at']

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        exclude = ['created_at', 'updated_at']