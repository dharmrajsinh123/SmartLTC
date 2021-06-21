from django.db import models

# Create your models here.
class Company(models.Model):
    id=models.AutoField(primary_key=True)
    Company_name = models.CharField(max_length=90)
    license_no=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")
    added_on = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255)
    def __str__(self):
        return self.Company_name

