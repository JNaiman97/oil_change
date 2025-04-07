import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oil_change_tracker.settings')

app = Celery('oil_change_tracker')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()