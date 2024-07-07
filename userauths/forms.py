from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User,Profile

class UserRegisterForm(UserCreationForm):
    full_name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter the full Name"}))
    # username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter the full Name"}))
    # full_name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter the full Name"}))
    # full_name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter the full Name"}))


    class Meta:
        model=User
        fields=['full_name','username','email','phone','password1','password2']