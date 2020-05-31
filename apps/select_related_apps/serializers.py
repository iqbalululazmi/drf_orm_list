from rest_framework import serializers
from .models import Vehicle, Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    customer_name = serializers.SerializerMethodField()

    def get_customer_name(self, obj):
        print(obj.customer)
        return obj.customer.name
    
    class Meta:
        model = Vehicle
        fields = '__all__'