from django.contrib import admin
from .models import Hotel,Booking,ActivityLog,StaffOnDuty,Room,RoomType
# Register your models here.


class HotelAdmin(admin.ModelAdmin):
    list_display = ['thumbnail','name','user','status']
    prepopulated_fields={'slug':('name',)}


admin.site.register(Hotel,HotelAdmin)
admin.site.register(Booking)
admin.site.register(ActivityLog)
admin.site.register(StaffOnDuty)
admin.site.register(Room)
admin.site.register(RoomType)