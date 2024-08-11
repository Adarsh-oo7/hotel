from django.shortcuts import render,redirect
from django.contrib.auth.decorators import  login_required
from django.db import models
from hotel.models import Hotel, Booking, ActivityLog, StaffOnDuty, Room, RoomType ,Coupon,Notification

# Create your views here.

@login_required
def dashboard(request):
    bookings = Booking.objects.filter(user=request.user,payment_status="Paid")
    total_spent = Booking.objects.filter(user=request.user,payment_status='Paid').aggregate(amount=models.Sum("total"))
    print(bookings)

    context={
        'bookings':bookings,
        'total_spent': total_spent
    }

    return render(request, 'user_dashboard/dashboard.html',context)