from parkinglot.drivers.serializers import DriverAgeResponseSerializer

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