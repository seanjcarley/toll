from importlib.util import module_for_loader
from django.db import models
from django_countries.fields import CountryField

# Create your models here.
class VehicleOwnerDetails(models.Model):
    ''' vehcile owner details from authority '''

    class Meta:
        verbose_name_plural = 'VehicleOwnerDetails'

    
    f_name = models.CharField(max_length=50, null=True, blank=True)
    s_name = models.CharField(max_length=50, null=True, blank=True)
    address_1 = models.CharField(max_length=75, null=False, blank=False)
    address_2 = models.CharField(max_length=75, null=True, blank=True)
    address_3 = models.CharField(max_length=75, null=True, blank=True)
    town_city = models.CharField(max_length=75, null=False, blank=False)
    county = models.CharField(max_length=30, null=True, blank=True)
    post_code = models.CharField(max_length=10, null=True, blank=True)
    country = CountryField(blank_label='Country', null=False, blank=False)


class VehicleDetails(models.Model):
    ''' vehicle details from authority '''

    class Meta:
        verbose_name_plural = 'VehicleDetails'

    
    owner = models.ForeignKey(
        VehicleOwnerDetails, null=False, 
        blank=False, on_delete=models.CASCADE)
    lpn = models.CharField(max_length=12, null=False, blank=False)
    make = models.CharField(max_length=30, null=False, blank=False)
    model = models.CharField(max_length=30, null=False, blank=False)
    color = models.CharField(max_length=30, null=False, blank=False)
    lpn_class = models.IntegerField(null=False, blank=False, default=1)
    start_date = models.DateTimeField(null=False, blank=False)
    end_date = models.DateTimeField(null=False, blank=False)
    update_date = models.DateTimeField(
        null=False, blank=False, 
        auto_now_add=True)
    seq_no = models.IntegerField(null=False, blank=False, default=1)
    scrapped = models.BooleanField(default=False)

    def __str__(self):
        return f'LPN: {self.lpn}'
