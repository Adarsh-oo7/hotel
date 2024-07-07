from django.shortcuts import render,redirect
from .models import User,Profile
from .forms import UserRegisterForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
# Create your views here.

def RegisterView(request):
    if request.user.is_authenticated:
        messages.warning(request,f'your are already loged in')
    form=UserRegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        full_name=form.cleaned_data.get('full_name')
        phone=form.cleaned_data.get('phone')
        email=form.cleaned_data.get('email')
        password=form.cleaned_data.get('password')

        user=authenticate(email=email,password=password)
        login(user)

        messages.success(request,f"hey {full_name} your account has been created successfully.")

        profile=Profile.objects.get(user=request.user)
        profile.full_name=full_name
        profile.phone=phone
        profile.save()
        
        return redirect('/')


        print(full_name)
    context={
        'form':form

    }
    return render(request,'userauths/sign-up.html', context)
