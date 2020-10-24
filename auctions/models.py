from django.contrib.auth.models import AbstractUser
from django.db import models

# model for users
class User(AbstractUser):
    username = models.CharField(max_length=64, unique=True)
    email = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=64)

# model for listings
class Listing(models.Model):
    seller = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    description = models.TextField()
    category = models.CharField(max_length=64, default=None)
    starting_bid = models.IntegerField(default=0)
    URL = models.CharField(
        max_length=200, default=None)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
