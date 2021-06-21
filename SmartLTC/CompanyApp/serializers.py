from rest_framework import serializers

from CompanyApp.models import Company
from rest_framework.serializers import ModelSerializer


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'