from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    book = models.FileField(upload_to='books/')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book.path.split('/')[-1]}"
