# Generated by Django 4.1 on 2022-09-02 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0002_alter_userprofile_country_alter_userprofile_county_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name_plural': 'UserProfile'},
        ),
        migrations.AlterModelOptions(
            name='uservehicle',
            options={'verbose_name_plural': 'UserVehicle'},
        ),
    ]