from django.shortcuts import render,redirect
from .models import User,Profile
from .forms import UserRegisterForm
from django.contrib.auth import authenticate,login,logout
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
        password=form.cleaned_data.get('password1')

        user=authenticate(email=email,password=password)
        login(request,user)

        messages.success(request,f"hey {full_name} your account has been created successfully.")

        profile=Profile.objects.get(user=request.user)
        profile.full_name=full_name
        profile.phone=phone
        profile.save()
        
        return redirect('/')


    context={
        'form':form

    }
    return render(request,'userauths/sign-up.html', context)

def logOut(request):
    logout(request)
    messages.success(request,'You have been logged out')
    return redirect('hotel:index')

def loginViewTem(request):
    if request.user.is_authenticated:
        print('hellow')
        messages.warning(request,'your are already logged in')
        return redirect('hotel:index')
    
    if request.POST:
        email=request.POST.get('email')
        password=request.POST.get('password')

        try:
            user_query=User.objects.get(email=email)
            user_auth=authenticate(request,email=email,password=password)
            if user_query is not None:
                login(request,user_auth)
                messages.success(request,'You are logged in')
                next_url=request.GET.get('next','index')
                return redirect(next_url)
            else:
                messages.error(request,'username or password does not exist')
                return redirect('userauths:sign-in')


        except:
            messages.error(request,'username or password does not exist')
            return redirect('userauths:sign-in')
        
    return render(request,'userauths/login.html')
