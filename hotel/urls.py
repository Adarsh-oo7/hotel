from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('hotel',views.hotel,name='hotel_page')
]
