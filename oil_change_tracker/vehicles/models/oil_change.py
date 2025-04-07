from django.db import models
from .vehicle import Vehicle

class OilChangeRecord(models.Model):
    vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE, related_name="oil_changes")
    date = models.DateField(blank=True, null=True)
    kilometrage = models.PositiveIntegerField(blank=True, null=True)
    next_reminder = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.vehicle.name} - {self.date}"