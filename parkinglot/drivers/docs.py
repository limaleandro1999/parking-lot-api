from parkinglot.drivers.serializers import (
    DriverAgeResponseSerializer, 
    DriverRemoveCarBodySerializer, 
    DriverRemoveCarResponseSerializer,
)

driver_cars_schema = dict(
    operation_description="Return all driver cars",
    responses={
        404: "Driver not found."
    }
)

driver_age_schema = dict(
    operation_description="Return the driver's age",
    responses={
        200: DriverAgeResponseSerializer,
        404: "Driver not found."
    }
)

driver_remove_car_schema = dict(
    request_body=DriverRemoveCarBodySerializer,
    responses={
        200: DriverRemoveCarResponseSerializer
    }
)