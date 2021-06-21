# Generated by Django 2.2.6 on 2021-06-21 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DeliveryApp', '0003_auto_20210621_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_mst',
            name='id',
        ),
        migrations.AddField(
            model_name='user_mst',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='DeliveryApp.User'),
        ),
    ]