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

class DriverAgeResponseSerializer(serializers.Serializer):
    age = serializers.IntegerField()

class DriverRemoveCarBodySerializer(serializers.Serializer):
    car_id = serializers.IntegerField()

class DriverRemoveCarResponseSerializer(serializers.Serializer):
    removed = serializers.BooleanField()
    car = CarSerializer(many=False)