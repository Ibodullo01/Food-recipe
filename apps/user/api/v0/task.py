
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.core.cache import cache
import random

@shared_task
def send_verification_email(user_email):
    verification_code = random.randint(100000, 999999)
    cache.set(f'verification_code_{user_email}', verification_code, timeout=60)  # 60 sekund

    send_mail(
        'Tasdiqlash kodingiz',
        f'Sizning tasdiqlash kodingiz: {verification_code}',
        settings.DEFAULT_FROM_EMAIL,
        [user_email],
        fail_silently=False,
    )
