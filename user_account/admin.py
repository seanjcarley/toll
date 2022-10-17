from django.contrib import admin
from .models import UserProfile, UserVehicle

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'account_no', 'street1', 'street2', 'street3', 
        'town_city', 'post_code', 'country', 'phone', 'date_added',
        'date_removed', 'update_date',
    )

    ordering = ('id',)


class UserVehicleAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'account','vehicle_id', 'lpn', 'make', 'model', 'color', 'lpn_class', 
        'date_added', 'date_removed', 'update_date',
    )

    ordering = ('id',)


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserVehicle, UserVehicleAdmin)
