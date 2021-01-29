from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete
from django.dispatch import receiver


class Book(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=settings.AUTH_USER_MODEL)
    book = models.FileField(upload_to='books')

    def __str__(self):
        return f"{self.book.name.split('/')[-1]}"


@receiver(pre_delete, sender=Book)
def delete_book(sender, instance, **kwargs):
    try:
        book = instance.book
    except AttributeError:
        return
    book.delete()
