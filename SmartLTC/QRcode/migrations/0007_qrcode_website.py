# Generated by Django 3.1.7 on 2021-05-14 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QRcode', '0006_auto_20210514_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrcode',
            name='website',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]