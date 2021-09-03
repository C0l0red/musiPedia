from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from uuid import uuid4
# Create your models here.

class CustomUserManager(UserManager):

    def create(self, username: str, email: str, password:str, **kwargs: Any):
        return self.create_user(username, email, password, **kwargs)


class User(AbstractUser):
    id = models.UUIDField(max_length=36, primary_key=True, editable=False, default=uuid4)
    email = models.EmailField(max_length=120, unique=True)
    avatar = models.URLField()

    objects = CustomUserManager()


