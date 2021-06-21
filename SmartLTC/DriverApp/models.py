from django.db import models

# Create your models here.
one_to_five_choices = zip(range(1,5+1), range(1,5+1))

class Driver(models.Model):
    driver_id=models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=90)
    last_name = models.CharField(max_length=90)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=111, default="")
    picture = models.ImageField(upload_to='DriverApp/images',default="")
    promo_code = models.CharField(max_length=111)
    rating = models.PositiveSmallIntegerField(choices=one_to_five_choices)
    activation_status = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name