from django.shortcuts import render,redirect,HttpResponse
from .models import Hotel, Booking, ActivityLog, StaffOnDuty, Room, RoomType ,Coupon,Notification,Bookmark
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import stripe 
from datetime import datetime
from django.urls import reverse
from django.http import JsonResponse
from decimal import Decimal
from django.utils import timezone



# Create your views here.


def index(request):
    hotels=Hotel.objects.filter(status='Live')
    context={
        'hotels':hotels
    }
    return render(request,'hotel/hotel.html',context)


def hotel_detail(request,slug):
    hotel=Hotel.objects.get(status='Live',slug=slug)

    if request.user.is_authenticated:
        bookmark = Bookmark.objects.filter(user=request.user, hotel=hotel)

    context={
        'hotel':hotel,
        'bookmark':bookmark
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

        if request.method=='POST':
            for h_id,item in request.session['selection_data_obj'].items():
                id = int(item['hotel_id'])
                checkin = item['checkin']
                checkout = item['checkout']
                adult = int(item['adult'])
                children = int(item['children'])
                room_type_= int(item['room_type'])
                room_id = int(item['room_id'])

                user = request.user
                hotel = Hotel.objects.get(id=id)
                room= Room.objects.get(id=room_id)
                room_type= RoomType.objects.get(id=room_type_)

            date_format ="%Y-%m-%d"
            checkin_date= datetime.strptime(checkin,date_format)
            checkout_date = datetime.strptime(checkout,date_format)
            time_diffrence= checkout_date - checkin_date
            total_days_= time_diffrence.days
     

            full_name=request.POST['full_name']
            email=request.POST['email']
            phone=request.POST['phone']

            booking = Booking.objects.create(
                hotel=hotel,
                room_type=room_type,
                check_in_date=checkin,
                check_out_date=checkout,
                total_days=total_days_,
                num_adults=adult,
                num_children=children,
                full_name=full_name,
                email=email,
                phone=phone,
                user=request.user or None,
                payment_status="Processing"
            )

            # if request.user.is_authenticated:
            #     booking.user=request.user
            #     booking.save()
            # else:
            #     booking.user == None
            #     booking.save()

            for h_id,item in request.session['selection_data_obj'].items():
                room_id = int(item['room_id'])
                room = Room.objects.get(id=room_id)
                booking.room.add(room)

                room_count += 1
                days = total_days_
                price = room_type.price

                room_price = price * room_count
                total = room_price * days

            booking.total += float(total)
           
            booking.before_discount += float(total)
            booking.save()

            messages.success(request, "check out Now")

            return redirect('hotel:checkout',booking.booking_id)
            
           

            





        hotel = None
        for h_id,item in request.session['selection_data_obj'].items():
            id = int(item['hotel_id'])
            checkin = item['checkin']
            checkout = item['checkout']
            adult = int(item['adult'])
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
   


def checkout(request, booking_id):
    booking = Booking.objects.get(booking_id=booking_id)
    if request.method == "POST":

        code = request.POST.get('code')
        
        try:
            coupon = Coupon.objects.get(code__iexact=code, active= True)
            if coupon in booking.coupons.all():
                print('coupon is alredy taken')
                messages.warning(request,"Coupon already Activate")
                return redirect('hotel:checkout', booking.booking_id)
            else:
                if coupon.type == 'percentage':
                    discount = booking.total * coupon.discount / 100
                else:
                    discount = coupon.discount

                booking.coupons.add(coupon)
                booking.total -= discount
                booking.saved += discount
                booking.save()
                print("coupon is valid")
                messages.success(request, 'Coupon Activated')
                return redirect('hotel:checkout', booking.booking_id)
        except:
            print("coupon does not esists")
            messages.error(request,"Coupon doesn't exist")
            return redirect('hotel:checkout', booking.booking_id)


        
    
    context= {

        'booking':booking,
        'stripe_publishable_key':settings.STRIPE_PUBLIC_KEY,

    }
    return render(request,'hotel/checkout.html',context)




@csrf_exempt
def create_checkout_session(request,booking_id):
    booking = Booking.objects.get(booking_id= booking_id)
    stripe.api_key = settings.STRIPE_SECRET_KEY

    checkout_session = stripe.checkout.Session.create(
        customer_email= booking.email,
        payment_method_types=['card'],
        line_items=[
            {
                'price_data':{
                    'currency':'USD',
                    'product_data':{
                        'name':booking.full_clean
                    },
                    'unit_amount':int(booking.total*100)
                },
                'quantity':1
            }
        ],
        mode='payment',
        success_url=request.build_absolute_uri(reverse("hotel:success", args=[booking.booking_id])) + '?session_id{CHECKOUT_SESSION_ID}&success_id='+booking.success_id+'&booking_total='+str(booking.total),cancel_url=request.build_absolute_uri(reverse("hotel:failed", args=[booking.booking_id]))
    )

    booking.payment_status = 'Processing'
    booking.strip_payment_intent = checkout_session['id']
    booking.save()

    print('check session', checkout_session)
    return JsonResponse({'sessionId':checkout_session.id})

 
def payment_SUCCESS(request,booking_id):
    success_id = request.GET.get('success_id')
    booking_total = request.GET.get('booking_total')

    if success_id and booking_id:
        success_id = success_id.rstrip('/')
        booking_total = booking_total.rstrip('/')

        booking = Booking.objects.get(booking_id= booking_id,success_id=success_id)

        if booking.total == Decimal(booking_total):
            if booking.payment_status == "Processing":      
                booking.payment_status = "Paid"
                booking.is_active = True
                booking.save()

                noti= Notification.objects.create(
                    booking=booking,
                    type="Booking Confirmed",

                )
                if request.user.is_authenticated:
                    noti.user = request.user
                else:
                    noti.user = None
                noti.save()


                if 'selection_data_obj' in request.session:
                    del request.session['selection_data_obj']




            else:
                messages.success(request,"Payment made already, thanks for your patronage")
        else:
            messages.error(request,"hotel/payment_success.html")

    context={
        'booking':booking
    }

    return render(request,'hotel/payment_success.html',context)

def payment_faild(request,booking_id):
    return HttpResponse("Payment failed")

@csrf_exempt
def update_room_status(request):
    today = timezone.now().date()

    booking = Booking.objects.filter(is_acitve=True, payment_status="Paid")
    for b in booking:
        if b.checked_in_tracker != True:
            if b.check_in_date> today:
                b.checked_in_tracker = False
                b.check_in = False
                b.save()

                for r in b.room.all():
                    r.is_available = True
                    r.save()
            
            else:
                b.checked_in_tracker = True
                b.check_in = True
                b.save()

                for r in b.room.all():
                    r.is_available = False
                    r.save()
        
        else:
            if b.check_out_date>today:
                b.checked_out_tracker = False
                b.check_in = False
                b.save()

                for r in b.room.all():
                    r.is_available = False
                    r.save()
            
            else:
                b.check_out_date = True
                b.check_in = True
                b.save()

                for r in b.room.all():
                    r.is_available = True
                    r.save()

    return HttpResponse(today)

    

