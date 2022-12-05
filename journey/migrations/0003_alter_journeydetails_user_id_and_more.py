# Generated by Django 4.1 on 2022-11-30 13:13

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vehicles', '0007_alter_vehicledetails_end_date'),
        ('journey', '0002_alter_tollchargedetails_valid_to_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journeydetails',
            name='user_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='journeydetails',
            name='vehicle_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicledetails'),
        ),
        migrations.AlterField(
            model_name='tollchargedetails',
            name='valid_to',
            field=models.DateTimeField(default=datetime.datetime(2032, 11, 17, 13, 13, 6, 762381)),
        ),
    ]
