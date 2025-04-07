from django.db import models
from django.conf import settings

class Vehicle(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)
    engine = models.CharField(max_length=100, blank=True, null=True)
    photo = models.ImageField(upload_to='vehicle_photos/', blank=True, null=True)

    def __str__(self):
        return self.name