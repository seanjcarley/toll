from django.contrib import admin
from .models import VehicleDetails, VehicleOwnerDetails

# Register your models here.
class VehicleDetailsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'owner', 'lpn', 'make', 'model', 'color', 'lpn_class', 
        'start_date', 'end_date', 'update_date', 'seq_no', 'scrapped'
    )

    ordering = ('id',)


class VehicleOwnerDetailsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'f_name', 's_name', 'address_1', 'address_2', 'address_3', 
        'town_city', 'county', 'post_code', 'country'
    )

    ordering = ('id',)


admin.site.register(VehicleDetails, VehicleDetailsAdmin)
admin.site.register(VehicleOwnerDetails, VehicleOwnerDetailsAdmin)