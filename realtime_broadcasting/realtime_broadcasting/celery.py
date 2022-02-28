import os 
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'realtime_broadcasting.settings')

app = Celery('realtime_broadcasting')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'get_joke_3s': {
        'task': 'joke.tasks.get_joke',
        'schedule': 3.0 # [sec]
    }
}
app.autodiscover_tasks()

