from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('User', 'User'),
        ('Engineer', 'Engineer'),
    )

    phone = models.CharField(max_length=15, blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='User')

    def __str__(self):
        return self.username