from rest_framework import serializers

# from DriverApp.models import Driver
from rest_framework.serializers import ModelSerializer

# from SmartLTC.DriverApp.models import Driver
from SmartLTC.DriverApp.models import Driver


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'