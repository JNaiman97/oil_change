from celery import shared_task
from django.core.mail import send_mail
from django.utils.timezone import now
from vehicles.models import OilChangeRecord

def send_reminder_emails():
    today = now().date()
    due_records = OilChangeRecord.objects.filter(next_reminder=today)

    for record in due_records:
        user_email = record.vehicle.owner.email
        if user_email:
            send_mail(
                subject='Oil Change Reminder',
                message=f"Hi {record.vehicle.owner.username}, it's time to change the oil for your vehicle: {record.vehicle.name}.",
                from_email='jakubnaiman97@gmail.com',
                recipient_list=[user_email],
                fail_silently=False,
            )