from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'hotel/hotel.html')



def hotel(request):
    return render(request,'hotel\hotel_page.html')