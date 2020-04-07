from rest_framework import viewsets

from parkinglot.cars.models import Car
from parkinglot.cars.serializers import CarSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.select_related('driver').all()
    serializer_class = CarSerializer