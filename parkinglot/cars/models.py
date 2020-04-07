from django.db import models

from parkinglot.drivers.models import Driver

class Car(models.Model):
    plate = models.CharField(max_length=7)
    model = models.CharField(max_length=40)
    manufacturing_year = models.CharField(max_length=4)
    model_year = models.CharField(max_length=4)
    driver = models.ForeignKey(
        Driver, 
        on_delete=models.CASCADE, 
        related_name='cars', 
        related_query_name='car'
    )

    def __str__(self):
        return f'{self.model} {self.manufacturing_year}/{self.model_year} - Plate: {self.plate}'