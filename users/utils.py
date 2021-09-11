from django.core.mail import send_mail
from django.conf import settings

import secrets


def generate_token():
    return str(secrets.token_hex(50))


def send_verification_message(email, token):
    # HOST_URL = "http://localhost:8000/"     # On development
    HOST_URL = "https://pdfstack.herokuapp.com/"    # On production
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


def send_password_reset_message(email, token):
    # HOST_URL = "http://localhost:8000/"     # On development
    HOST_URL = "https://pdfstack.herokuapp.com/"    # On production
    VERIFICATION_URL = f"account/password/reset/confirm/?token={token}"
    URL = HOST_URL + VERIFICATION_URL
    SUBJECT = "Password Reset"
    MESSAGE = f"""Hi There!
Someone has requested a password reset on PDFStack using this email, if
it was you please click on the link below:


{URL}


or just copy and paste it into a browser.
"""
    send_mail(
        SUBJECT, 
        MESSAGE,
        settings.EMAIL_HOST_USER, [email, ],
        fail_silently=False
    ) 
