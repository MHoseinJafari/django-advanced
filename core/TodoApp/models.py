from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=35)

    ON_GOING = 1
    DONE = 2
    task_status = (
        (ON_GOING, "در حال انجام"),
        (DONE, "تمام شده"),
    )

    status = models.IntegerField(choices=task_status)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    