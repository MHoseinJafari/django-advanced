from rest_framework.test import APIClient
import pytest
from django.urls import reverse
from accounts.models import User
from TodoApp.models import Task
from datetime import datetime


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def common_user():
    user = User.objects.create_user(
        email="mohammad@gmail.com", password="m@1234567", is_verified=True
    )
    return user


@pytest.fixture
def task_data():
    data = {
        "name": "test task",
        "status": 1,
        "created_date": datetime.now(),
    }
    return data


@pytest.fixture
def task_create():
    data = {
        "name": "test task",
        "status": 1,
        "created_date": datetime.now(),
    }
    task_obj = Task.objects.create(**data)
    return task_obj


@pytest.mark.django_db
class TestTaskApi:
    def test_get_task_response_200_status(self, api_client):
        url = reverse("todoapp:api-v1:task-list")
        response = api_client.get(url)
        assert response.status_code == 200

    def test_create_task_response_201_status(
        self, api_client, common_user, task_data
    ):
        url = reverse("todoapp:api-v1:task-list")
        user = common_user
        api_client.force_login(user=user)
        response = api_client.post(url, task_data, format="json")
        assert response.status_code == 201
        task = Task.objects.first()
        assert task is not None
        assert Task.objects.count() == 1
        assert Task.objects.all()[0].name == "test task"

    def test_create_task_unauthorized_response_401_status(
        self, api_client, task_data
    ):
        url = reverse("todoapp:api-v1:task-list")
        response = api_client.post(url, task_data, format="json")
        assert response.status_code == 401

    def test_create_task_no_status_bad_request_response_400_status(
        self, api_client, common_user
    ):
        url = reverse("todoapp:api-v1:task-list")
        data = {
            "name": "test task",
        }
        user = common_user
        api_client.force_login(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 400

    def test_put_task_response_200_status(
        self, api_client, task_create, common_user
    ):
        url = reverse("todoapp:api-v1:task-detail", args=[task_create.id])
        data = {
            "name": "test task edited by put",
            "status": 2,
        }
        user = common_user
        api_client.force_login(user=user)
        response = api_client.put(url, data, format="json")
        assert response.status_code == 200
        assert Task.objects.all()[0].name == "test task edited by put"
        assert Task.objects.all()[0].status == 2

    def test_put_task_unauthorized_response_401_status(
        self, api_client, task_create
    ):
        url = reverse("todoapp:api-v1:task-detail", args=[task_create.id])
        data = {
            "name": "test task edited by put",
            "status": 2,
        }

        response = api_client.put(url, data, format="json")
        assert response.status_code == 401
        assert Task.objects.all()[0].status == 1

    def test_put_task_bad_request_response_400_status(
        self, api_client, task_create, common_user
    ):
        url = reverse("todoapp:api-v1:task-detail", args=[task_create.id])
        data = {
            "name": "test task edited by put",
        }
        user = common_user
        api_client.force_login(user=user)
        response = api_client.put(url, data, format="json")
        assert response.status_code == 400
        assert Task.objects.all()[0].status == 1

    def test_patch_task_respone_200_status(
        self, api_client, common_user, task_create
    ):
        url = reverse("todoapp:api-v1:task-detail", args=[task_create.id])
        data = {"name": "test edited by patch"}
        user = common_user
        api_client.force_login(user)
        response = api_client.patch(url, data, format="json")
        assert response.status_code == 200
        assert Task.objects.all()[0].status == 1
        assert Task.objects.all()[0].name == "test edited by patch"

    def test_patch_task_unauthorized_respone_401_status(
        self, api_client, task_create
    ):
        url = reverse("todoapp:api-v1:task-detail", args=[task_create.id])
        data = {"name": "test edited by patch"}
        response = api_client.patch(url, data, format="json")
        assert response.status_code == 401
        assert Task.objects.all()[0].status == 1
        assert Task.objects.all()[0].name != "test edited by patch"

    def test_delete_task_response_204_status(
        self, api_client, common_user, task_create
    ):
        url = reverse("todoapp:api-v1:task-detail", args=[task_create.id])
        user = common_user
        api_client.force_login(user)
        response = api_client.delete(url)
        assert response.status_code == 204
        assert Task.objects.count() == 0
        task = Task.objects.first()
        assert task is None

    def test_delete_task_unauthorized_response_401_status(
        self, api_client, task_create
    ):
        url = reverse("todoapp:api-v1:task-detail", args=[task_create.id])
        response = api_client.delete(url)
        assert response.status_code == 401
        assert Task.objects.count() == 1
        task = Task.objects.first()
        assert task is not None
