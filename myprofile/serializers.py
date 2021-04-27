from rest_framework import serializers
from .models import *


class ProfileDesignerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileDesigner
        fields = '__all__'


class ProfileCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileCustomer
        fields = '__all__'

