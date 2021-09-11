from django.core.mail import send_mail
from django.conf import settings

import secrets


def generate_token():
    return str(secrets.token_hex(120))


def send_verification_message(email, token):
    HOST_URL = "http://localhost:8000/"
    VERIFICATION_URL = f"account/email/verify/confirm/?token={token}"
    URL = HOST_URL + VERIFICATION_URL
    SUBJECT = "Email Confirmation"
    MESSAGE = f"""Hi There!
Thank you for trying to verify your email, you're just one step away to verify your code.
please click on the link below to verify your email:


{URL}


or just copy and paste it into a browser.
"""
    send_mail(
        SUBJECT, 
        MESSAGE,
        settings.EMAIL_HOST_USER, [email, ],
        fail_silently=False
    ) 
