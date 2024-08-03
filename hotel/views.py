from django.shortcuts import render,redirect
from .models import Hotel, Booking, ActivityLog, StaffOnDuty, Room, RoomType 
from django.contrib import messages

from datetime import datetime
# Create your views here.


def index(request):
    hotels=Hotel.objects.filter(status='Live')
    context={
        'hotels':hotels
    }
    return render(request,'hotel/hotel.html',context)


def hotel_detail(request,slug):
    hotel=Hotel.objects.get(status='Live',slug=slug)
    context={
        'hotel':hotel
    }
    return render(request,'hotel/hotel_page.html',context)

def room_type_detail(request, slug,rt_slug):
    hotel =Hotel.objects.get(status='Live', slug=slug)
    room_type= RoomType.objects.get(hotel=hotel,slug=rt_slug)
    rooms= Room.objects.filter(room_type=room_type, is_available=True)

    id=request.GET.get('hotel-id')
    checkin=request.GET.get('checkin')
    checkout=request.GET.get('checkout')
    adutl=request.GET.get('adult')
    children=request.GET.get('children')






    print('id===',id)

    context={
        'hotel':hotel,
        'room_type':room_type,
        'rooms':rooms,
        'checkin':checkin,
        'checkout':checkout,
        'adult':adutl,
        'children':children

    }
    return render(request,'hotel/room_type_detail.html',context)


def selected_rooms(request):
    total=0
    room_count=0
    total_days=0
    adult=0
    children=0
    checkin=""
    checkout=""


    if 'selection_data_obj' in request.session:
        hotel = None
        for h_id,item in request.session['selection_data_obj'].items():
            id = int(item['hotel_id'])
            checkin = item['checkin']
            checkout = item['checkout']
            children = int(item['children'])
            room_type= int(item['room_type'])
            room_id = int(item['room_id'])

            room_type = RoomType.objects.get(id=room_type)

            date_format ="%Y-%m-%d"
            checkin_date= datetime.strptime(checkin,date_format)
            checkout_date = datetime.strptime(checkout,date_format)
            time_diffrence= checkout_date - checkin_date
            total_days= time_diffrence.days

            room_count += 1
            days = total_days
            price = room_type.price

            room_price = price * room_count
            total = room_price * days


            hotel = Hotel.objects.get(id = id)
        
        context ={
            'data':request.session['selection_data_obj'],
            'total_selected_items':len(request.session['selection_data_obj']),
            'total':total,
            'total_days':total_days,
            'adult':adult,
            'children':children,
            'checkin':checkin,
            'checkout':checkout,
            'hotel':hotel


        }

        return render(request,'hotel/selected_rooms.html',context)

    else:
        messages.warning(request, 'no selected rooms yet')
        return redirect('/')
   


