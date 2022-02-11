from django import forms

from society.models import Flat

class FlatForm(forms.ModelForm):
    class Meta:
        model = Flat
        exclude = ['created_at', 'updated_at']