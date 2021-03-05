from django.db import models

class Driver(models.Model):
    name = models.CharField(max_length=255, null=False)
    license = models.CharField(max_length=32, null=False)

    def __str__(self):
        return f'{self.name}, {self.license}'
