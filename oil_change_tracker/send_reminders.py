import os
import django

# Nastavení prostředí Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oil_change_tracker.settings")
django.setup()

from django.core.mail import send_mail
from django.utils import timezone
from vehicles.models import OilChangeRecord


def send_reminders():
    today = timezone.now().date()
    reminders = OilChangeRecord.objects.filter(next_reminder=today)

    for record in reminders:
        send_mail(
            'Oil Change Reminder',
            f'Hello! This is your oil change reminder for your vehicle {record.vehicle.name}. Have a nice day!',
            'jakubnaiman97@gmail.com',  # FROM
            [record.vehicle.owner.email],  # TO
            fail_silently=False,
        )

if __name__ == "__main__":
    send_reminders()