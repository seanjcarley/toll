# Generated by Django 4.1 on 2022-09-20 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0005_alter_uservehicle_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='uservehicle',
            name='account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user_account.userprofile'),
        ),
    ]
