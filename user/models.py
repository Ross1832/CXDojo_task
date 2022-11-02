from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField()
    created_at = models.DateField(auto_now_add=True)

