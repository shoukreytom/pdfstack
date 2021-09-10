from users.utils import validate_username
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']
    
    def clean_username(self):
        username = self.cleaned_data['username']
        validate_username(username)
        return username
