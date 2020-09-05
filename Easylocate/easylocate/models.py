from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


from djmoney.models.fields import MoneyField

from .managers import CustomUserManager

# Create your models here.

class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Custom User model"""
    email = models.EmailField(unique=True, max_length=255, verbose_name='email address')
    name = models.CharField(max_length=70)
    is_active = models.BooleanField(default=True)
    is_admin= models.BooleanField(default=False)

    objects = CustomUserManager

    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name


class Hostel(models.Model):
    name = models.CharField(max_length=70)
    image = models.ImageField(upload_to="images/%Y/%m/%d", height_field=200, width_field=200)
    description = models.TextField()
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='NGN')

    def __str__(self):
        return self.name


class MyHostels(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)

    def __str__(self):
        return self.user



  




