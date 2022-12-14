# Generated by Django 4.1 on 2022-11-30 14:38

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('journey', '0003_alter_journeydetails_user_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journeydetails',
            name='toll_road_detailsID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journey.tollroaddetails'),
        ),
        migrations.AlterField(
            model_name='tollchargedetails',
            name='valid_to',
            field=models.DateTimeField(default=datetime.datetime(2032, 11, 17, 14, 38, 10, 437450)),
        ),
    ]
