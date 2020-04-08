from datetime import date

from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response

from parkinglot.drivers.models import Driver
from parkinglot.drivers.serializers import DriverSerializer
from parkinglot.cars.serializers import CarSerializer

from parkinglot.drivers.docs import (
    driver_cars_schema,
    driver_age_schema,
    driver_remove_car_schema,
)

class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    car_serializer_class = CarSerializer

    def get_serializer_class(self):
        if self.action == 'cars' or self.action == 'remove_car':
            return self.car_serializer_class
        return super().get_serializer_class()

    @swagger_auto_schema(**driver_cars_schema)
    @action(detail=False, methods=["get"], url_path="(?P<pk>[^/.]+)/cars")
    def cars(self, request, pk=None):
        driver = self.get_object()
        cars = driver.cars.all()
        
        serializer = self.get_serializer(cars, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(**driver_age_schema)
    @action(detail=False, methods=["get"], url_path="(?P<pk>[^/.]+)/age")
    def age(self, request, pk=None):
        driver = self.get_object()
        today = date.today()
        age = today.year - driver.birth_date.year
        return Response({'age': age})

    @swagger_auto_schema(**driver_remove_car_schema)
    @action(detail=False, methods=["post"], url_path="(?P<pk>[^/.]+)/remove_car")
    def remove_car(self, request, pk=None):
        driver = self.get_object()
        car_id = request.data.get('car_id')

        try:
            car = driver.cars.get(id=car_id)
            car_serialized = self.get_serializer(car, many=False)
            return Response({'removed': True, 'car': car_serialized.data})
        except:
            return Response(data={'removed': False, 'car': None}, status=status.HTTP_400_BAD_REQUEST)