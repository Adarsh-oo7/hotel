from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('detail/<slug>/',views.hotel_detail,name='hotel_detail')

]
