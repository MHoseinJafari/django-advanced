from django.core.management.base import BaseCommand
from TodoApp.models import Task
from faker import Faker

from datetime import datetime
import random


class Command(BaseCommand):
    help = "create a test task and test faker module"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.faker = Faker()

    def handle(self, *args, **options):
        for _ in range(5):
            Task.objects.create(
                name=self.faker.job(),
                status=random.choice([1, 2]),
                created_date=datetime.now(),
            )
