from django.http import HttpResponse

from .tasks import SendEmail


def send_email(request):
    SendEmail.delay()
    return HttpResponse("<h1>Email sent</h1>")
