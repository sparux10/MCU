from django.db import models
from  superuser.models import MyUser
# Create your models here.

class Address(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    street = models.CharField(max_length=200, blank=True, null=True)
    postal_code = models.CharField(max_length=6, blank=True, null=True)

    def __str__(self):
        return f"{self.user.email}'s address"

class UserProfile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def __str__(self):
        return self.user.email
