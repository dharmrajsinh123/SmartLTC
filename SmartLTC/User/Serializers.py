from random import randint

from django.contrib.auth.password_validation import validate_password
from django.core.mail import send_mail
from rest_framework import serializers
from rest_framework.authtoken.admin import User
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator

from .models import User
#
# from SmartLTC.User.models import Account


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
        # fields = '__all__'

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        # fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

# # Register Serializer driver with extra fields
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = driver
#         fields = ('id', 'username', 'email')
        # fields = '__all__'
# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = driver
#         fields = ( 'username','driver_id','first_name','last_name','phone_number' ,'email', 'password')
#         # fields = '__all__'
#         extra_kwargs = {'password': {'write_only': True}}
#
#     def create(self, validated_data):
#         user = User.objects.create(
#             username=validated_data['username'],
#             email=validated_data['email'],
#             first_name=validated_data['first_name'],
#             last_name=validated_data['last_name'],
#             # phone_number=validated_data['phone_number']
#         )
#
#         user.set_password(validated_data['password'])
#         user.save()
#
#         return user
#
# class ChangePasswordSerializer(serializers.Serializer):
#     model = driver
#
#     """
#     Serializer for password change endpoint.
#     """
#     old_password = serializers.CharField(required=True)
#     new_password = serializers.CharField(required=True)

# class RegisterSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(
#         required=True,
#         validators=[UniqueValidator(queryset=User.objects.all())]
#     )
#
#     password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
#     password2 = serializers.CharField(write_only=True, required=True)
#
#     class Meta:
#         model = driver
#         # fields = ('username',  'email', 'first_name','last_name','password', 'password2',)
#         fields = '__all__'
#         extra_kwargs = {
#             'first_name': {'required': True},
#             'last_name': {'required': True},
#             # 'phone_number': {'required': True},
#         }
#
#     def validate(self, attrs):
#         if attrs['password'] != attrs['password2']:
#             raise serializers.ValidationError({"password": "Password fields didn't match."})
#
#         return attrs
#
    # def create(self, validated_data):
    #     user = driver.objects.create(
    #         # username=validated_data['username'],
    #         email=validated_data['email'],
    #         first_name=validated_data['first_name'],
    #         last_name=validated_data['last_name'],
    #         # phone_number=validated_data['phone_number']
    #     )
    #
    #     user.set_password(validated_data['password'])
    #     user.save()
    #
    #     return user



# class AccountSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Demo
#         fields = '__all__'

# from rest_framework import serializers
# from django.contrib.auth.models import User
# from rest_framework.validators import UniqueValidator
# from django.contrib.auth.password_validation import validate_password
#
#
# class RegisterSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(
#         required=True,
#         validators=[UniqueValidator(queryset=User.objects.all())]
#     )
#
#     password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
#     password2 = serializers.CharField(write_only=True, required=True)
#
#     class Meta:
#         model = User
#         fields = ('username', 'password', 'password2', 'email','first_name', 'last_name')
#         extra_kwargs = {
#             'first_name': {'required': True},
#             'last_name': {'required': True},
#
#         }
#
#     def validate(self, attrs):
#         if attrs['password'] != attrs['password2']:
#             raise serializers.ValidationError({"password": "Password fields didn't match."})
#
#         return attrs
#
#     def create(self, validated_data):
#         user = User.objects.create(
#             username=validated_data['username'],
#             email=validated_data['email'],
#             first_name=validated_data['first_name'],
#             last_name=validated_data['last_name'],
#
#         )
#
#         user.set_password(validated_data['password'])
#         user.save()
#
#         return user