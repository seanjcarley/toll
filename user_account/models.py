from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from vehicles.models import VehicleDetails


# Create your models here.
class UserProfile(models.Model):
    ''' user profile for contact details '''

    class Meta:
        verbose_name_plural = 'UserProfile'
    

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_no = models.IntegerField(null=False, blank=False)
    street1 = models.CharField(max_length=75, null=False, blank=False)
    street2 = models.CharField(max_length=75, null=True, blank=True)
    street3 = models.CharField(max_length=75, null=True, blank=True)
    town_city = models.CharField(max_length=75, null=False, blank=False)
    county = models.CharField(max_length=30, null=False, blank=False)
    post_code = models.CharField(max_length=10, null=True, blank=True)
    country = CountryField(blank_label='Country', null=False, blank=True, default='Ireland')
    phone = models.CharField(max_length=20, null=True, blank=True)
    date_added = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    date_removed = models.DateTimeField(null=True, blank=True)
    update_date = models.DateTimeField(
        null=False, blank=False, 
        auto_now=True)

    def __str__(self):
        return self.user.username


class UserVehicle(models.Model):
    ''' user vehicle details '''

    class Meta:
        verbose_name_plural = 'UserVehicle'

    account = models.ForeignKey(UserProfile, null=False, 
                                    blank=False, on_delete=models.CASCADE, default=1)
    vehicle_id = models.OneToOneField(VehicleDetails, on_delete=models.CASCADE)
    lpn = models.CharField(max_length=12, null=False, blank=False)
    make = models.CharField(max_length=30, null=False, blank=False)
    model = models.CharField(max_length=30, null=False, blank=False)
    color = models.CharField(max_length=30, null=False, blank=False)
    lpn_class = models.IntegerField(null=False, blank=False)
    date_added = models.DateTimeField(null=False, blank=False,
                                        auto_now_add=True)
    date_removed = models.DateTimeField(null=True, blank=True)
    update_date = models.DateTimeField(null=False, blank=False, 
                                        auto_now=True)

    


# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     ''' creates a profile if none, or updates existing one '''
#     if created:
#         UserProfile.objects.create(user=instance)

#     # saves existing profile
#     instance.UserProfile.save()
