from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4
# Create your models here.

class User(AbstractUser):
    id = models.UUIDField(max_length=36, primary_key=True, editable=False, default=uuid4)
    email = models.EmailField(max_length=120, unique=True)
    image = models.URLField()

    class Meta:
        app_label = "modules"

