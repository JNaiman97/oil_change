import os
import django
from django.core.mail import send_mail
from django.utils import timezone
from yourapp.models import OilChangeRecord

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oil_change_tracker.settings")
django.setup()

def send_reminders():
    today = timezone.now().date()
    reminders = OilChangeRecord.objects.filter(next_reminder=today)

    for record in reminders:
        send_mail(
            'Oil Change Reminder',
            f'Hello! This is your oil change reminder for your vehicle {record.vehicle.name}. Have a nice day',
            'jakubnaiman97@gmail.com',  # Tvoje emailová adresa
            [record.vehicle.owner.email],  # Email vlastníka vozidla
            fail_silently=False,
        )

if __name__ == "__main__":
    send_reminders()