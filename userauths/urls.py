from django.urls import path
from . import views


urlpatterns = [
    path('',views.RegisterView,name="sign-up"),
    path('',views.logout,name='logout')
]
