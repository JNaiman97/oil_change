class OilChangeRecord(models.Model):
    vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE, related_name="oil_changes")
    date = models.DateField()
    mileage = models.PositiveIntegerField()
    next_reminder = models.DateField()

    def __str__(self):
        return f"{self.vehicle.name} - {self.date}"