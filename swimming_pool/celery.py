import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'swimming_pool.settings')

app = Celery('swimming_pool')


app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


app.conf.beat_schedule={
    'send_to_gmale': {
        'task':'apps.info.tasks.send_info_tg',
        'schedule': 60
    }
}


