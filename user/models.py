from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="email")
    full_name = models.CharField(max_length=150, verbose_name='full name')
    phone = models.IntegerField()
    group = models.CharField(max_length=50, blank=True, null=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


