from django.db import models

# Create your models here.

class Vehicle(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='vehicle_photos/', blank=True, null=True)

    def __str__(self):
        return self.name