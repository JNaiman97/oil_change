from celery import shared_task
from django.utils.timezone import now
from django.core.mail import send_mail
from vehicles.models import Vehicle

@shared_task
def send_oil_change_reminders():
    today = now().date()
    vehicles = Vehicle.objects.filter(next_reminder=today)
    for vehicle in vehicles:
        user = vehicle.owner
        send_mail(
            subject='Oil Change Reminder',
            message=f'Dear {user.username}, it is time to change the oil for your vehicle: {vehicle.name}.',
            from_email='noreply@example.com',
            recipient_list=[user.email],
            fail_silently=False,
        )