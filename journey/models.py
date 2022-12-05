from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from vehicles.models import VehicleDetails
from user_account.models import UserProfile
from datetime import datetime, timedelta

# Create your models here.
class TollChargeDetails(models.Model):
    ''' toll charges '''

    class Meta:
        verbose_name_plural = 'TollCharges'


    def set_future_datetime():
        return datetime.now() + timedelta(weeks=520)

    charge_name = models.CharField(max_length=25, null=False, blank=False)
    class_1_charge = models.DecimalField(null=False, blank=False, 
                        decimal_places=2, max_digits=5, default=0.0)
    class_2_charge = models.DecimalField(null=False, blank=False, 
                        decimal_places=2, max_digits=5, default=0.0)
    class_3_charge = models.DecimalField(null=False, blank=False, 
                        decimal_places=2, max_digits=5, default=0.0)
    class_4_charge = models.DecimalField(null=False, blank=False, 
                        decimal_places=2, max_digits=5, default=0.0)
    class_5_charge = models.DecimalField(null=False, blank=False, 
                        decimal_places=2, max_digits=5, default=0.0)
    class_6_charge = models.DecimalField(null=False, blank=False, 
                        decimal_places=2, max_digits=5, default=0.0)
    class_7_charge = models.DecimalField(null=False, blank=False, 
                        decimal_places=2, max_digits=5, default=0.0)
    penalty_1_charge = models.DecimalField(null=False, blank=False, 
                        decimal_places=2, max_digits=5, default=0.0)
    penalty_2_charge = models.DecimalField(null=False, blank=False, 
                        decimal_places=2, max_digits=5, default=0.0)
    valid_from = models.DateTimeField(null=False, blank=False)
    valid_to = models.DateTimeField(null=False, blank=False, 
                default=set_future_datetime())
    created_date = models.DateTimeField(null=False, blank=False, 
                    auto_now_add=True)
    update_date = models.DateTimeField(null=False, blank=False, 
                    auto_now=True)

    def __str__(self):
        return str(self.id)


class TollRoadDetails(models.Model):
    ''' toll road details '''

    class Meta:
        verbose_name_plural = 'TollRoadDetails'


    road_name = models.CharField(max_length=25, null=False, blank=False)
    road_toll_point_id = models.IntegerField(null=False, blank=False)
    road_toll_point_dir = models.CharField(max_length=5, null=False, 
                    blank=False)
    created_date = models.DateTimeField(null=False, blank=False, 
                    auto_now_add=True)
    update_date = models.DateTimeField(null=False, blank=False, 
                    auto_now=True)
    toll_charges_id = models.ForeignKey(TollChargeDetails, null=False, 
                        blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class JourneyDetails(models.Model):
    ''' journey details '''

    class Meta:
        verbose_name_plural = 'JourneyDetails'

    vehicle_ID = models.ForeignKey(VehicleDetails, null=False, blank=False,
                                on_delete=models.CASCADE)
    user_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    trip_date = models.DateTimeField(null=False, blank=False)
    post_date = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    toll_road_detailsID = models.ForeignKey(TollRoadDetails, null=False, 
                            blank=False, on_delete=models.CASCADE)
    paid = models.BooleanField(null=False, blank=False, default=False)
    created_date = models.DateTimeField(null=False, blank=False, 
                    auto_now_add=True)
    update_date = models.DateTimeField(null=False, blank=False, 
                    auto_now=True)

    def __str__(self):
        return str(self.id)

    

