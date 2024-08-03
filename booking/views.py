from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages
from hotel.models import Hotel, Booking, ActivityLog, StaffOnDuty, Room, RoomType 
from django.http import HttpResponseRedirect,JsonResponse
# Create your views here.
def check_room_availability(request):
    if request.POST:
        id = request.POST.get('hotel-id')
        checkin= request.POST.get('checkin')
        checkout=request.POST.get('checkout')
        adult=request.POST.get('adult')
        children= request.POST.get('children')
        room_type= request.POST.get('room_type')

        hotel= Hotel.objects.get(id=id)
        room_type=RoomType.objects.get(hotel=hotel,slug=room_type)

        url = reverse("room_type_detail",args=[hotel.slug,room_type.slug])
        url_with_params = f"{url}?hotel-id={id}&checkin={checkin}&checkout={checkout}&adult={adult}&children={children}&room_type={room_type}"
        return HttpResponseRedirect(url_with_params)
    

def add_to_selection(request):
    room_selection={}

    room_selection[str(request.GET['id'])]={
        'hotel_id':request.GET['hotel_id'],
        'hotel_name':request.GET['hotel_name'],
        'room_name':request.GET['room_name'],
        'room_price':request.GET['room_price'],
        'number_of_beds':request.GET['number_of_beds'],
        'room_number':request.GET['room_number'],
        'room_type':request.GET['room_type'],
        'room_id':request.GET['room_id'],
        'checkout':request.GET['checkout'],
        'checkin':request.GET['checkin'],
        'adult':request.GET['adult'],
        'children':request.GET['children'],
    }

    if 'selection_data_obj' in request.session:
        if str(request.GET['id'] in request.session['selection_data_obj']):
            selection_data=request.session['selection_data_obj']
            selection_data[str(request.GET['id'])]['adult']=int(room_selection[str(request.GET['id'])]['adult'])
            selection_data[str(request.GET['id'])]['children']=int(room_selection[str(request.GET['id'])]['children'])
            request.session['selection_data_obj']=selection_data
        else:
            selection_data=request.session['selection_data_obj']
            selection_data.update(room_selection)
    else:
        request.session['selection_data_obj']= room_selection


    data= {
        'data':request.session['selection_data_obj'],
        'total_selection_items': len(request.session['selection_data_obj'])

    }
    return JsonResponse(data)



