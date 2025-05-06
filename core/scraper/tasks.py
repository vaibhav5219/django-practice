from celery import shared_task # type: ignore
import time
import os
import requests

@shared_task
def add(x, y):
    time.sleep(5)
    return x+y

@shared_task
def download_image(image_url, save_directory, image_name):
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)
    image_path = os.path.join(save_directory, image_name)
    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        with open(image_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
    return image_path


''' Creating CELERY BEAT Tasks '''
from django_celery_beat.models import PeriodicTask, IntervalSchedule # type: ignore
from .models import Info

@shared_task
def create_info():
    Info.objects.create( info = "This is added by celery beat")
    
schedule, created = IntervalSchedule.objects.get_or_create(
    every = 1,
    period = IntervalSchedule.MINUTES   # every minute it will call
)

PeriodicTask.objects.update_or_create(
    name = "Create infor",
    defaults = {
        'task' : 'create_info',  # 'home.task.create_info',
        'interval' : schedule,
        'args' : '[]',  #   '['first', 'sec']'
    }
)