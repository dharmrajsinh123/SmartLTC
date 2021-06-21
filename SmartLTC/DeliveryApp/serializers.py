from rest_framework import serializers

# from DeliveryApp.models import store
from rest_framework.serializers import ModelSerializer

# from SmartLTC.DeliveryApp.models import store
# from SmartLTC.DeliveryApp.models import store
from .models import store,role_mst,user_mst

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = store
        fields = '__all__'

class role_mstSerializer(serializers.ModelSerializer):
    class Meta:
        model = role_mst
        fields = '__all__'

class user_mstSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_mst
        fields = '__all__'
