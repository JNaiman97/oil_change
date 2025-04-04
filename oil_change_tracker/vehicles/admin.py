from django.contrib import admin
from .models import Vehicle, OilChangeRecord

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'engine', 'photo')
    search_fields = ('name', 'owner__username')

@admin.register(OilChangeRecord)
class OilChangeRecordAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'date', 'kilometrage', 'next_reminder')
    search_fields = ('vehicle__name', 'vehicle__owner__username')

