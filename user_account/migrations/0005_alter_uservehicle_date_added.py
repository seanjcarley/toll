# Generated by Django 4.1 on 2022-09-20 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0004_alter_userprofile_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uservehicle',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
