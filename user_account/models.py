from itertools import filterfalse
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField

from vehicles.models import VehicleDetails


# Create your models here.
class UserProfile(models.Model):
    ''' user profile for contact details '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_no = models.IntegerField(null=False, blank=False)
    street1 = models.CharField(max_length=75, null=True, blank=True)
    street2 = models.CharField(max_length=75, null=True, blank=True)
    street3 = models.CharField(max_length=75, null=True, blank=True)
    town_city = models.CharField(max_length=75, null=True, blank=True)
    county = models.CharField(max_length=30, null=True, blank=True)
    post_code = models.CharField(max_length=10, null=True, blank=True)
    country = CountryField(blank_label='Country', null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)


    def __str__(self):
        return self.user.username


class UserVehicle(models.Model):
    ''' user vehicle details '''
    lpn = models.CharField(max_length=12, null=False, blank=False)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    ''' creates a profile if none, or updates existing one '''
    if created:
        UserProfile.objects.create(user=instance)

    # saves existing profile
    instance.UserProfile.save()
