from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManager()

    def __str__(self):
        return self.email


class EmailAddress(models.Model):
    email = models.EmailField(_("email address"), unique=True)
    token = models.CharField(max_length=120, unique=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='profile_images', default='profile_images/user-default.png')

    def __str__(self):
        return f'<Profile {self.user.email}>'
