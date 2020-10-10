from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import UserSignupForm


class UserSignup(CreateView):
    form_class = UserSignupForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/signup.html'


def profile(request):
    return render(request, 'users/profile.html')
