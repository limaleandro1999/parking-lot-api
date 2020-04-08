from datetime import date

from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.decorators import action

from parkinglot.cars.models import Car
from parkinglot.cars.serializers import CarSerializer
from parkinglot.cars.docs import park_car_schema, pays_ipva_car_schema

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.select_related('driver').all()
    serializer_class = CarSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^model', '^plate', '^driver__first_name']

    @swagger_auto_schema(**park_car_schema)
    @action(detail=True, methods=['post'], url_path="park")
    def park(self, request, pk=None):
        return Response({'message': f'{self.get_object()} was successfully parked'})

    @swagger_auto_schema(**pays_ipva_car_schema)
    @action(detail=True, methods=['get'], url_path="pays-ipva")
    def pays_ipva(self, request, pk=None):
        car = self.get_object()
        today = date.today()
        car_age = today.year - int(car.manufacturing_year)
        pays_ipva = True if car_age < 10 else False
        return Response({'pays_ipva': pays_ipva})