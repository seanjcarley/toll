# Generated by Django 4.1 on 2022-12-05 12:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journey', '0004_alter_journeydetails_toll_road_detailsid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tollchargedetails',
            name='valid_to',
            field=models.DateTimeField(default=datetime.datetime(2032, 11, 22, 12, 11, 14, 815970)),
        ),
    ]