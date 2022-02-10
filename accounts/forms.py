from django.forms import ModelForm
from accounts.models import CustomUser

class CustomUserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'aadhar', 'phone']
