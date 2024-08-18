from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User,Profile
from django.forms import FileInput
class UserRegisterForm(UserCreationForm):
    full_name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter the full Name",'class':"form-control"}))
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter the User Name",'class':'form-control'}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'placeholder':"Enter Your Email",'class':'form-control'}))
    phone=forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter Your phone",'class':'form-control'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':"password",'class':'form-control'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':"Conform Password",'class':'form-control'}))



    class Meta:
        model=User
        fields=['full_name','username','email','phone','password1','password2']




class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email']


class ProfileUpdateForm(forms.ModelForm):  
    class Meta:
        model = Profile
        fields = [
            "image",
            "full_name",
            "phone",
            "user",
            "gender",
            "country",
            "city",
            "state",
            "address",
            "identity_type",
            "identity_image",
            "facebook",
            "instagram"
         ]
        widgts ={
            'image':FileInput(attrs={"onchange" :"loadFile(event)", "class": "upload" })
        }


