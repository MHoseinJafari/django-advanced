from locust import HttpUser, task


class QuickstartUser(HttpUser):
    def on_start(self):
        response = self.client.post(
            "/accounts/api/v1/jwt/create/",
            data={
                "email": "mo@gmail.com",
                "password": "m@12345678",
            },
        ).json()
        self.client.headers = {
            "authorization": f"Bearer {response.get('access', None)}"
        }

    @task
    def task_list(self):
        self.client.get("/TodoApp/api/v1/task/")

    @task
    def task_post(self):
        self.client.post(
            "/TodoApp/api/v1/task/", data={"name": "task", "status": 1}
        )
