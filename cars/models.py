from django.db import models
from drivers.models import Driver

class Car(models.Model):
    brand = models.CharField(max_length=255, null=False)
    model = models.CharField(max_length=255, null=False)
    year = models.IntegerField(null=False)
    vin = models.CharField(max_length=64, null=False)
    owner = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.brand} {self.model}'