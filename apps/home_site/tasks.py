from celery import shared_task
from django.core.mail import send_mail

from apps.home_site.models import SiteInfo

email1 = SiteInfo.objects.get(id = 1).email

@shared_task
def send_message(self: str, text: str):
    send_mail(
        'Заголовок',
        text,
        email1,
        [*self],
        fail_silently=False,
    )