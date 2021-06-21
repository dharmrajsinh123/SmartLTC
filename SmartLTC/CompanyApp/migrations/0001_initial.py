# Generated by Django 3.1.7 on 2021-05-11 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Company_name', models.CharField(max_length=90)),
                ('license_no', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=111)),
                ('state', models.CharField(max_length=111)),
                ('zip_code', models.CharField(max_length=111)),
                ('phone', models.CharField(default='', max_length=111)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
    ]
