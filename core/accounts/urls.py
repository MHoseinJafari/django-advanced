from django.urls import path, include
from . import views

app_name = "accounts"

urlpatterns = [
    path("send-email/", views.send_email, name="send-email"),
    path("weather/", views.WeatherTestView, name="weather-test"),
    path("", include("django.contrib.auth.urls")),
    path("api/v1/", include("accounts.api.v1.urls")),
]
