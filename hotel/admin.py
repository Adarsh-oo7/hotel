from django.contrib import admin
from .models import Hotel,Booking,ActivityLog,StaffOnDuty,Room,RoomType,HotelGallery,Coupon,Notification,Bookmark
# Register your models here.

class HotelGalleryInline(admin.TabularInline):
    model=HotelGallery

class HotelAdmin(admin.ModelAdmin):
    inlines = [HotelGalleryInline]
    list_display = ['thumbnail','name','user','status']
    prepopulated_fields={'slug':('name',)}


admin.site.register(Hotel,HotelAdmin)
admin.site.register(Booking)
admin.site.register(ActivityLog)
admin.site.register(StaffOnDuty)
admin.site.register(Room)
admin.site.register(RoomType)
admin.site.register(Coupon)
admin.site.register(Notification)
admin.site.register(Bookmark)
