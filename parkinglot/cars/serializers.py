from rest_framework import serializers

from parkinglot.cars.models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class ParkCarBodySerializer(serializers.Serializer):
    pass

class ParkCarResponseSerializer(serializers.Serializer):
    message = serializers.CharField()

class CarPaysIpvaResponseSerializer(serializers.Serializer):
    pays_ipva = serializers.BooleanField()