from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User, BaseUserManager
from django.contrib import messages
from django.contrib.auth import authenticate

from .forms import UserSignupForm


class UserSignup(CreateView):
    form_class = UserSignupForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/signup.html'


@login_required
@require_http_methods(['GET', 'POST', ])
def profile(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        current_password = request.POST['currentPassword']
        new_password = request.POST['newPassword']
        confirm_password = request.POST['confirmPassword']
        user = authenticate(request, username=username, password=current_password)
        if user and new_password == confirm_password:
            user.email = email=BaseUserManager.normalize_email(email)
            user.set_password(new_password)
            user.save()
            messages.success(request, "your account information has been updated successfully!");
        else:
            messages.error(request, "passwords don't match.")
    return render(request, 'users/profile.html')
