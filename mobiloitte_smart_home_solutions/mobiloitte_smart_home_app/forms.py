from django import forms
from .models import *

class LoginForm(forms.ModelForm):
    class Meta:
        model = AppUser
        fields = "__all__"
