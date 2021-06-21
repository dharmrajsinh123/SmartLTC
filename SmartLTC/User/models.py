from random import random

from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.dispatch import receiver
from django.shortcuts import redirect
from rest_framework.authtoken.admin import User
# from django.contrib.auth.models import User
from django.db.models.signals import pre_save,post_save

# password_reset
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
# from django_rest_passwordreset.signals import password_reset_otp_created
from django.core.mail import send_mail
import uuid

# import math, random
@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token,  *args, **kwargs):
        email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key,)

        # otp = generateOTP() //for otp generate
        # email_plaintext_message = otp //for otp generate

        # OTP update for user (DB entry)
        send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "dharmrajsinh.dynamic.methods@gmail.com",
        # to:
        [reset_password_token.user.email]

    )
## //for otp generate
# function to generate OTP
# def generateOTP():
#     # Declare a string variable
#     # which stores all string
#     # string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     string = '0123456789'
#     OTP = ""
#     length = len(string)
#     for i in range(6):
#         OTP += string[math.floor(random.random() * length)]
#         if generateOTP==password_reset_token_created:
#             return redirect(' ')
#         else:
#             context={""}
#     return OTP

# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
#
# class driver(AbstractBaseUser):
#     driver_id=models.AutoField(primary_key=True)
#     username = models.CharField(max_length=30)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.CharField(max_length=255)
#     phone_number = models.CharField(max_length=111, default="")
#     picture = models.ImageField(upload_to='DriverApp/images',default="")
#     promo_code = models.CharField(max_length=10)
#     # rating = models.PositiveSmallIntegerField(choices=one_to_five_choices)
#     # activation_status = models.DateTimeField(auto_now_add=True)
#     password = models.CharField(max_length=65, default="")
#
#     # def __str__(self):
#     #     return self.first_name
# #
# USERNAME_FIELD = 'email'
# REQUIRED_FIELDS = ['username']
# #
# # # objects = MyAccountManager()
# #
# def __str__(self):
# 	return self.email
#
# 	# For checking permissions. to keep it simple all admin have ALL permissons
# def has_perm(self, perm, obj=None):
# 	return self.is_admin
#
# 	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
# def has_module_perms(self, app_label):
# 		return True