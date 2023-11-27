from celery import shared_task
from django_celery_beat.models import PeriodicTask, PeriodicTasks
from time import sleep


@shared_task
def SendEmail():
    sleep(3)
    print("done sending email")


@shared_task
def delete_task():
    PeriodicTask.objects.filter(enabled=True).exclude(
        name="celery.backend_cleanup"
    ).delete()
    PeriodicTasks.changed()
