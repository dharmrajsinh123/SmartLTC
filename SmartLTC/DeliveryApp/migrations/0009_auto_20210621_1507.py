# Generated by Django 2.2.6 on 2021-06-21 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DeliveryApp', '0008_auto_20210621_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_mst',
            name='role_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='DeliveryApp.role_mst'),
        ),
    ]