from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User, BaseUserManager
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import authenticate
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from .forms import UserSignupForm
from .utils import UsernameValidationError, validate_username


class UserSignup(SuccessMessageMixin, CreateView):
    form_class = UserSignupForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/signup.html'
    success_message = "your account has been created successfully! now login."


@login_required
@require_http_methods(['GET', 'POST', ])
def profile(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        try:
            validate_username(username)
            validate_email(email)
            current_password = request.POST['currentPassword']
            new_password = request.POST['newPassword']
            confirm_password = request.POST['confirmPassword']
            if not (new_password and confirm_password):
                user = request.user
                user.email = BaseUserManager.normalize_email(email)
                user.username = username
                user.save()
                messages.success(
                    request, "your account information has been updated successfully!")
            else:
                user = authenticate(request, username=username,
                                    password=current_password)
                if user:
                    if new_password == confirm_password:
                        user.email = email = BaseUserManager.normalize_email(email)
                        user.set_password(new_password)
                        user.save()
                        messages.success(
                            request, "your account information has been updated successfully!")
                    else:
                        messages.error(request, "password don't match.")
                else:
                    messages.error(request, "authentication failed!")
        except UsernameValidationError as e:
            messages.error(request, str(e))
        except ValidationError:
            messages.error(request, "invalid email or username.")
    return render(request, 'users/profile.html')
