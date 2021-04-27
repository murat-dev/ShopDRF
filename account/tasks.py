from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_activation_mail(email, activation_code):
    activation_url = f'http://127.0.0.1:8000/api/v1/account/activate/{activation_code}'
    message = f"""Thank you for registering. Activate your account using the link:{activation_url}"""
    send_mail(
        'Активация аккаунта',
        message,
        'test@my_project.com',
        [email, ],
    )


@shared_task
def send_activation_code(email, activation_code):
    activation_url = f'{activation_code}'
    message = f"""Restore password use code: {activation_url}"""
    send_mail(
        'Активация аккаунта',
        message,
        'test@my_project.com',
        [email, ],
    )

