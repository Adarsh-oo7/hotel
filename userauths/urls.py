from django.urls import path
from . import views


urlpatterns = [
    path('sign-up',views.RegisterView,name="sign-up"),
    path('sign-in',views.loginViewTem,name="sign-in"),
    path('',views.logOut,name='logOut')

 
]
