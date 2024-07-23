from django.shortcuts import render,redirect
from django.urls import reverse
from hotel.models import Hotel, Booking, ActivityLog, StaffOnDuty, Room, RoomType 

# Create your views here.
def check_room_availability(request):
    if request.POST:
        id = request.POST.get('hotel-id')
        checkin= request.POST.get('checkin')
        checkout=request.POST.get('checkout')
        adult=request.POST.get('adult')
        childred= request.POST.get('children')
        room_type= request.POST.get('room_type')

        hotel= Hotel.objects.get(id=id)
        room_type=RoomType.objects.get(hotel=hotel,slug=room_type)

        url = reverse("hotel:room_type_detail",args=[hotel.slug,room_type.slug])
        url_with_params = f"{url}?hotel-id={id}&checkin={checkin}&checkout={checkout}"