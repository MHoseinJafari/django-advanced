from celery import shared_task
from django_celery_beat.models import PeriodicTask
from time import sleep

"""
this tasks run by celery and redis.
this is a test for running a periodic task

"""


@shared_task
def SendEmail():
    sleep(3)
    print("done sending email")


@shared_task
def delete_task():
    names = ["celery.backend_cleanup", "delete task"]
    print(PeriodicTask.objects.all())
    PeriodicTask.objects.all().exclude(name__in=names).delete()
