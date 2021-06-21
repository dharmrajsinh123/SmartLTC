import uuid

from location_field.models.plain import PlainLocationField
from django.db import models

# Create your models here.


class store(models.Model):
    id = models.AutoField(primary_key=True)
    # store_code = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    store_code = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    store_name = models.CharField(max_length=90)
    store_address = models.CharField(max_length=90)
    store_phone = models.CharField(max_length=15, null=False)
    store_email = models.EmailField(max_length=255,null=False)

    # long =models.DecimalField(max_digits=9, decimal_places=6)
    # lat = models.DecimalField(max_digits=9, decimal_places=6)

    store_city = models.CharField(max_length=111)
    store_location = PlainLocationField(based_fields=['store_city'], zoom=7)

    # latitude = models.FloatField(null=True, default=None, verbose_name="location latitude")
    # longitude = models.FloatField(null=True, default=None, verbose_name="location longitude")

    store_logo= models.ImageField(upload_to='DeliveryApp/images',default="")
    Active_Status = 1
    Inactive_Status = 0
    STATUS_CHOICES = (
        (Active_Status, 'Active'),
        (Inactive_Status, 'Inactive'),
    )
    is_status = models.IntegerField(choices=STATUS_CHOICES, default=Active_Status)
    # is_status = models.CharField(max_length=111)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    # license_no=models.CharField(max_length=255)

    # address = models.CharField(max_length=255)
    # city = models.CharField(max_length=111)
    # is_state = models.CharField(max_length=111)
    #
    # phone = models.CharField(max_length=111, default="")
    # added_on = models.DateTimeField(auto_now_add=True)
    # description = models.CharField(max_length=255)
    def __str__(self):
        return self.store_name

class patient(models.Model):
    id = models.AutoField(primary_key=True)
    # patient_code = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient_code = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    patient_fname = models.CharField(max_length=90)
    patient_lname = models.CharField(max_length=90)
    patient_phone = models.CharField(max_length=15, null=False)
    patient_email = models.EmailField(max_length=255,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient_fname


class home(models.Model):
    id = models.AutoField(primary_key=True)
    home_code=models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    # home_code =models.CharField(default=uuid.uuid4().hex[:5].upper(), max_length=50, editable=False)
    home_name = models.CharField(max_length=90)
    home_address = models.CharField(max_length=90)
    home_city = models.CharField(max_length=90)
    home_phone = models.CharField(max_length=15, null=False)
    home_email = models.EmailField(max_length=255,null=False)

    # city = models.CharField(max_length=111)
    home_location = PlainLocationField(based_fields=['home_city'], zoom=7)

    home_logo = models.ImageField(upload_to='DeliveryApp/images', default="")
    Active_Status = 1
    Inactive_Status = 0
    STATUS_CHOICES = (
        (Active_Status, 'Active'),
        (Inactive_Status, 'Inactive'),
    )
    is_status = models.IntegerField(choices=STATUS_CHOICES, default=Active_Status)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    # home_location = models.FloatField(max_length=100,unique=True)
    # home_location=models.CharField(max_length=100,unique=True)
    # latitude = PlainLocationField(based_fields=['city'], zoom=7)
    # longitude = PlainLocationField(based_fields=['city'], zoom=7)


    def __str__(self):
        return self.home_name

class driver(models.Model):
    id = models.AutoField(primary_key=True)
    driver_code = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    # models.CharField(primary_key=True, default=uuid.uuid4().hex[:5].upper(), max_length=50, editable=False)

    # driver_code = models.CharField(max_length=6,null=False)
    driver_fname = models.CharField(max_length=90)
    driver_lname = models.CharField(max_length=90)
    driver_address = models.CharField(max_length=90)
    driver_city = models.CharField(max_length=90)
    driver_phone = models.CharField(max_length=15, null=False)
    driver_email = models.EmailField(max_length=255, null=False)
    driver_location = PlainLocationField(based_fields=['driver_city'], zoom=7)
    driver_photo = models.ImageField(upload_to='DeliveryApp/images', default="")
    Active_Status = 1
    Inactive_Status = 0
    STATUS_CHOICES = (
        (Active_Status, 'Active'),
        (Inactive_Status, 'Inactive'),
    )
    is_status = models.IntegerField(choices=STATUS_CHOICES, default=Active_Status)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.driver_fname

class role_mst(models.Model):
    id = models.AutoField(primary_key=True)
    role_code = models.CharField(max_length=90)
    rol_name = models.CharField(max_length=90)
    Active_Status = 1
    Inactive_Status = 0
    STATUS_CHOICES = (
       (Active_Status, 'Active'),
       (Inactive_Status, 'Inactive'),
    )
    is_active = models.IntegerField(choices=STATUS_CHOICES, default=Active_Status)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return self.role_code

class user_driver_map(models.Model):
    id = models.AutoField(primary_key=True)
    user_code=models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    driver_code=models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    Active_Status = 1
    Inactive_Status = 0
    STATUS_CHOICES = (
        (Active_Status, 'Active'),
        (Inactive_Status, 'Inactive'),
    )
    is_active = models.IntegerField(choices=STATUS_CHOICES, default=Active_Status)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return self.user_code

class user_pharmacy_map(models.Model):
    id = models.AutoField(primary_key=True)
    user_code=models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    store_code=models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    Active_Status = 1
    Inactive_Status = 0
    STATUS_CHOICES = (
        (Active_Status, 'Active'),
        (Inactive_Status, 'Inactive'),
    )
    is_active = models.IntegerField(choices=STATUS_CHOICES, default=Active_Status)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return self.user_code

class user_home_map(models.Model):
    id = models.AutoField(primary_key=True)
    user_code = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    home_code = models.UUIDField(primary_key=False,default=uuid.uuid4, editable=False)
    Active_Status = 1
    Inactive_Status = 0
    STATUS_CHOICES =(
        (Active_Status, 'Active'),
        (Inactive_Status, 'Inactive'),
    )
    is_active = models.IntegerField(choices=STATUS_CHOICES,default=Active_Status)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.home_code

class user_patient_map(models.Model):
    id = models.AutoField(primary_key=True)
    user_code = models.UUIDField(primary_key=False, default=uuid.uuid4,editable=False)
    patient_code = models.UUIDField(primary_key=False,default=uuid.uuid4,editable=False)
    Active_Status = 1
    Inactive_Status = 0
    STATUS_CHOICES =(
        (Active_Status,'Active'),
        (Inactive_Status,'Inactive'),
    )
    is_active = models.IntegerField(choices=STATUS_CHOICES,default=Active_Status)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient_code

class order_mst(models.Model):
    id = models.AutoField(primary_key=True)
    order_code = models.UUIDField(primary_key=False,default=uuid.uuid4,editable=False)
    Active_Status = 1
    Inactive_Status = 0
    STATUS_CHOICES = (
        (Active_Status, 'Active'),
        (Inactive_Status, 'Inactive'),
    )
    is_active = models.IntegerField(choices=STATUS_CHOICES, default=Active_Status)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_code

class order_packet_map(models.Model):
    id = models.AutoField(primary_key=True)
    order_code = models.UUIDField(primary_key=False,default=uuid.uuid4,editable=False)
    packet_code = models.UUIDField(primary_key=False,default=uuid.uuid4,editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.packet_code

class packet_mst (models.Model):
    id = models.AutoField(primary_key=True)
    packet_code = models.UUIDField(primary_key=False,default=uuid.uuid4,editable=False)
    packet_qrcode =models.TextField()
    home_location = models.FloatField(max_length=100, unique=True)
    delivery_location = models.FloatField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.packet_code

class job_mst(models.Model):
    id = models.AutoField(primary_key=True)
    job_code = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    Active_Status = 1
    Inactive_Status = 0
    STATUS_CHOICES = (
        (Active_Status, 'Active'),
        (Inactive_Status, 'Inactive'),
    )
    is_active = models.IntegerField(choices=STATUS_CHOICES, default=Active_Status)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.job_code

class job_packet_map(models.Model):
    id = models.AutoField(primary_key=True)
    job_code = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    packet_code = models.UUIDField(primary_key=False,default=uuid.uuid4,editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.packet_code

class job_list(models.Model):
    id = models.AutoField(primary_key=True)
    job_code = models.UUIDField(primary_key=False,default=uuid.uuid4,editable=False)
    Active_Status = 1
    Inactive_Status = 0
    STATUS_CHOICES = (
        (Active_Status, 'Active'),
        (Inactive_Status, 'Inactive'),
    )
    is_active = models.IntegerField(choices=STATUS_CHOICES, default=Active_Status)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.job_code

class job_driver_map(models.Model):
    id = models.AutoField(primary_key=True)
    user_code = models.UUIDField(primary_key=False,default=uuid.uuid4,editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_code

class vehical_type(models.Model):
    id = models.AutoField(primary_key=True)
    vehical_type_code = models.UUIDField(primary_key=False,default=uuid.uuid4,editable=False)
    vehical_type = models.CharField(max_length=90)
    vehical_type_desc = models.CharField(max_length=500)
    vehical_type_img = models.ImageField(upload_to='DeliveryApp/Vehical_type/images',default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vehical_type_code

class driver_vehical(models.Model):
    id = models.AutoField(primary_key=True)
    driver_code = models.UUIDField(primary_key=False,default=uuid.uuid4,editable=False)
    vehical_type_code = models.UUIDField(primary_key=False,default=uuid.uuid4,editable=False)
    vehical_number = models.CharField(max_length=15, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.driver_code


class user_mst(models.Model):
    user_code = models.UUIDField(primary_key=False,default=uuid.uuid4,editable=False)
    username = models.CharField(max_length=90)
    password = models.CharField(max_length=65, default="")
    role_code = models.ForeignKey(role_mst,on_delete=models.CASCADE,primary_key=True)
    promo_code = models.CharField(max_length=111)
    ref_promo_code = models.CharField(max_length=111)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_code



