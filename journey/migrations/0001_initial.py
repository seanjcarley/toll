# Generated by Django 4.1 on 2022-11-24 14:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vehicles', '0005_alter_vehicledetails_update_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='TollChargeDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charge_name', models.CharField(max_length=25)),
                ('class_1_charge', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('class_2_charge', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('class_3_charge', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('class_4_charge', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('class_5_charge', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('class_6_charge', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('class_7_charge', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('penalty_1_charge', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('penalty_2_charge', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('valid_from', models.DateTimeField()),
                ('valid_to', models.DateTimeField(default='9999-12-31 23:59:59.999')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'TollCharges',
            },
        ),
        migrations.CreateModel(
            name='TollRoadDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('road_name', models.CharField(max_length=25)),
                ('road_toll_point_id', models.IntegerField()),
                ('road_toll_point_dir', models.CharField(max_length=5)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('toll_charges_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='journey.tollchargedetails')),
            ],
            options={
                'verbose_name_plural': 'TollRoadDetails',
            },
        ),
        migrations.CreateModel(
            name='JourneyDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_date', models.DateTimeField()),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('toll_road_detailsID', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('user_ID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vehicle_ID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicledetails')),
            ],
            options={
                'verbose_name_plural': 'JourneyDetails',
            },
        ),
    ]