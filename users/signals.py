from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from users.models import User

from .models import Profile

@receiver(post_save, sender=User)
def save_profile(sender, instance=None, created=False, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)
