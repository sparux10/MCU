from django.db.models.signals import post_save
from django.dispatch import receiver
from account.models import *



@receiver(post_save, sender=MyUser)
def my_callback(sender, instance, created, **kwargs):
    if created:
            Address.objects.create(user=instance)


@receiver(post_save, sender=MyUser)
def my_callback(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

