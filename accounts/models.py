from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from society.models import Flat

from .managers import CustomUserManager

# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20,  null=True, blank=True)
    email = models.EmailField(unique=True, primary_key=True)
    occupation = models.CharField(max_length=20, null=True, blank=True)
    phone = models.PositiveIntegerField(unique=True)
    aadhar = models.PositiveIntegerField(unique=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'

class Owner(models.Model):
    flat = models.OneToOneField(Flat, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    address = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.name

class Tenant(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

