# Generated by Django 3.1.7 on 2021-05-13 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QRcode', '0003_auto_20210513_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcode',
            name='qr_code',
            field=models.ImageField(blank=True, upload_to='qr_codes'),
        ),
    ]