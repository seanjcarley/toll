# Generated by Django 4.1 on 2022-09-02 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehicledetails',
            options={'verbose_name_plural': 'VehicleDetails'},
        ),
        migrations.AlterModelOptions(
            name='vehicleownerdetails',
            options={'verbose_name_plural': 'VehicleOwnerDetails'},
        ),
    ]