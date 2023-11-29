from django.http import HttpResponse, JsonResponse
from django.views.decorators.cache import cache_page

from .tasks import SendEmail
import requests


def send_email(request):
    SendEmail.delay()
    return HttpResponse("<h1>Email sent</h1>")


@cache_page(60 * 20)
def WeatherTestView(request):
    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?lat=37.268219&lon=49.589123&appid=9be11538ceebf4c5d0ee0c5d97579881"
    )
    return JsonResponse(response.json())
