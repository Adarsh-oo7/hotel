from django.shortcuts import render,redirect
from django.contrib.auth.decorators import  login_required
from django.db import models
from django.contrib import messages

from hotel.models import Hotel, Booking, ActivityLog, StaffOnDuty, Room, RoomType ,Coupon,Notification,Bookmark
from django.http import JsonResponse
# Create your views here.

@login_required
def dashboard(request):
    bookings = Booking.objects.filter(user=request.user,payment_status="Paid")
    total_spent = Booking.objects.filter(user=request.user,payment_status='Paid').aggregate(amount=models.Sum("total"))
    

    context={
        'bookings':bookings,
        'total_spent': total_spent
    }

    return render(request, 'user_dashboard/dashboard.html',context)


@login_required
def bookings(request):
    bookings= Booking.objects.filter(user=request.user,payment_status="Paid")
    context={
        'bookings':bookings
    }
    return render(request,"user_dashboard/bookings.html",context)




@login_required
def booking_detail(request,booking_id):
    booking= Booking.objects.get(booking_id=booking_id, user=request.user,payment_status="Paid")
    context={
        'booking':booking
    }
    return render(request,"user_dashboard/booking_detail.html",context)
    


@login_required
def notifications(request):
    notifications =Notification.objects.filter(user=request.user,seen=False)

    context = {
        'notifications':notifications
    }
    return render(request,"user_dashboard/notification.html",context)
    

def notification_mark_as_seen(request, id):
    noti = Notification.objects.get(id=id)
    noti.seen = True
    noti.save()
    messages.success(request,"Notification Seen")

    return redirect("user_dashboard:notifucations")

@login_required
def wallet(request):
    bookings = Booking.objects.filter(user=request.user,payment_status="Paid")
    total_spent = Booking.objects.filter(user=request.user,payment_status='Paid').aggregate(amount=models.Sum("total"))
    wallet_balance = request.user.profile.wallet

    context={
        'bookings':bookings,
        'total_spent': total_spent,
        'wallet_balance':wallet_balance
    }

    return render(request, 'user_dashboard/wallet.html',context)


@login_required
def bookmark(request):
    bookmark = Bookmark.objects.filter(user=request.user)  
   
    return render(request,'user_dashboard/bookmark.html', {'bookmark':bookmark})


def delete_bookmark(request,bid):
    bookmark = Bookmark.objects.get(bid=bid)
    bookmark.delete()
    messages.success(request,"Notification seen")
    return redirect('user_dashboard:bookmark')

def add_to_bookmark(request):
    id = request.GET.get('id')
    hotel = Hotel.objects.get(id=id)
    if request.user.is_authenticated:
        bookmark = Bookmark.objects.filter(user=request.user, hotel=hotel)
        if bookmark.exists():
            bookmark = Bookmark.objects.get(user=request.user, hotel=hotel)
            bookmark.delete()
            return JsonResponse({"data":"Bookmark Deleted", 'icon':'success'})
        else:
            Bookmark.objects.create(user=request.user, hotel=hotel)
            return JsonResponse({"data":"Hotel Bookmarked", 'icon':'success'})
    else:
         return JsonResponse({'data':"Login To Bookmark Hotel",'icon':"success"})
