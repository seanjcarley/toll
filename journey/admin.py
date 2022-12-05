from django.contrib import admin
from .models import TollChargeDetails, JourneyDetails, TollRoadDetails

# Register your models here.
class TollRoadDetailsAdmin(admin.ModelAdmin):
    '''  '''
    list_display = (
        'id', 'road_name', 'road_toll_point_id', 'road_toll_point_dir', 
        'created_date', 'update_date', 'toll_charges_id'
    )

    ordering = ('id',)


class JourneyDetailsAdmin(admin.ModelAdmin):
    '''  '''
    list_display = (
        'id', 'vehicle_ID', 'user_ID', 'trip_date', 'post_date', 
        'toll_road_detailsID', 'created_date', 'update_date'
    )

    ordering = ('post_date', 'trip_date', 'id',)


class TollChargeDetailsAdmin(admin.ModelAdmin):
    '''  '''

    list_display = (
        'id', 'charge_name', 'class_1_charge', 'class_2_charge', 'class_3_charge', 
        'class_4_charge', 'class_5_charge', 'class_6_charge', 
        'class_7_charge', 'penalty_1_charge', 'penalty_2_charge', 
        'valid_from', 'valid_to', 'created_date', 'update_date'
    )

    ordering = ('id',)


admin.site.register(TollRoadDetails, TollRoadDetailsAdmin)
admin.site.register(JourneyDetails, JourneyDetailsAdmin)
admin.site.register(TollChargeDetails, TollChargeDetailsAdmin)
