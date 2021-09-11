from users.models import EmailAddress


def check_email_verification(request):
    is_verified = False
    if request.user.is_authenticated:
        email_addr = EmailAddress.objects.filter(email=request.user.email)
        if email_addr:
            is_verified = email_addr[0].is_verified
    return {"user_is_verified": is_verified}
