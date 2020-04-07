from rest_framework import serializers

from parkinglot.drivers.models import Driver
from parkinglot.cars.models import Car

from parkinglot.cars.serializers import CarSerializer

class DriverSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True)

    class Meta:
        model = Driver
        fields = '__all__'
    
    def validate_cpf(self, value):
        if len(value) is not 11:
            raise serializers.ValidationError('CPF is invalid')
        return value