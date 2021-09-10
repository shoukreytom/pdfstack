from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import BaseUserManager
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import authenticate, login
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from users.models import User
from users.forms import AddUserForm


class UserSignup(SuccessMessageMixin, CreateView):
    form_class = AddUserForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/signup.html'
    success_message = "your account has been created successfully! now login."


@login_required
@require_http_methods(['GET', 'POST', ])
def profile(request):
    if request.method == 'POST':
        email = request.POST.get('email', None)
        new_password = request.POST.get('newPassword', None)
        confirm_password = request.POST.get('confirmPassword', None)
        current_password = request.POST.get('currentPassword', None)
        if email:
            try:
                validate_email(email)
                count = User.objects.filter(email=email)
                if count and email != request.user.email:
                    messages.error(request, "This email is already exists.")
                else:
                    request.user.email = BaseUserManager.normalize_email(email)
                    request.user.save()
                    messages.success(request, "Your account information has been updated successfully.")
                    user = request.user
                    login(request, user)
            except ValidationError:
                messages.error(request, "Invalid email.")
        if new_password:
            if new_password == confirm_password:
                user = authenticate(request, email=request.user.email,
                                    password=current_password)
                if not user:
                    messages.error(request, "Authentication failed.")
                else:
                    user.email = BaseUserManager.normalize_email(email)
                    user.set_password(new_password)
                    user.save()
                    login(request, user)
            else:
                messages.error(request, "Password don't match.")
    return render(request, 'users/profile.html')
