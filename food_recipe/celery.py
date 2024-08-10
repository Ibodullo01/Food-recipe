

from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food_recipe.settings')

app = Celery('food_recipe')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
