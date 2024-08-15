from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

app_name = "user_dashboard"


urlpatterns = [
    path("",views.dashboard, name="dashboard"),
    path('booking-detail/<booking_id>',views.booking_detail,name="booking_detail"),
    path('booking/',views.bookings,name="bookings"),
    path('notifications/',views.notifications,name="notifications"),
    path('notification_mark_as_seen/<id>',views.notification_mark_as_seen,name="notification_mark_as_seen"),
    path('wallet/',views.wallet,name="wallet"),
    path('bookmark/',views.bookmark,name="bookmark"),
    path('delete_bookmark/<bid>',views.delete_bookmark,name="delete_bookmark"),
    path('add_to_bookmark/',views.add_to_bookmark,name="add_to_bookmark"),
    path('profile/',views.profile,name="profile"),

    path("change-password/",auth_view.PasswordChangeView.as_view(template_name="user_dashboard/password-reset/change-password.html",success_url="/dashboard/password_changed"),name="change_password"),
    path('password_changed/',views.password_changed,name='password_changed')



]


