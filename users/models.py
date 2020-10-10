from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='profile_images', default='profile_images/user-default.png')

    def __str__(self):
        return f'<Profile {self.user.username}>'
