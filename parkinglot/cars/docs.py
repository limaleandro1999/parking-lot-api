from parkinglot.cars.serializers import (
    ParkCarBodySerializer, 
    ParkCarResponseSerializer, 
    CarPaysIpvaResponseSerializer
)

park_car_schema = dict(
    request_body=ParkCarBodySerializer,
    responses={
        201: ParkCarResponseSerializer
    }
)

pays_ipva_car_schema = dict(
    responses={
        200: CarPaysIpvaResponseSerializer
    }
)