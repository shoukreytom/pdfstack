from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver


class Book(models.Model):
    book = models.FileField(upload_to='books')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book.name.split('/')[-1]}"


@receiver(post_delete, sender=Book)
def delete_book(sender, instance, **kwargs):
    instance.book.delete()
