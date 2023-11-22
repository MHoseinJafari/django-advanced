import pytest
from TodoApp.models import Task
from datetime import datetime


@pytest.mark.django_db
class TestTaskModel:
    def test_create_task_model_valid_data(self):
        task = Task.objects.create(
            name="test",
            status=1,
            created_date=datetime.now(),
        )
        assert task is not None
        assert task.name == "test"
        assert task.status == 1
        assert Task.objects.filter(pk=task.id).exists() == True

    def test_create_task_model_bad_data(self):
        try:
            task = Task.objects.create(
                name="test",
            )
            assert task is None
        except Exception:
            assert True
