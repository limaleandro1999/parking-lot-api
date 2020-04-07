from django.db import models

class Driver(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  birth_date = models.DateField()
  cpf = models.CharField(unique=True, max_length=11)

  def __str__(self):
      return f'{self.first_name} {self.last_name}'

