from uuid import uuid4
from django.db import models


class Artist(models.Model):
    id = models.UUIDField(max_length=36, primary_key=True, editable=False, default=uuid4)
    real_name = models.CharField(max_length=80)
    stage_name = models.CharField(max_length=80, unique=True)
    record_label = models.CharField(max_length=120)
    date_of_birth = models.DateField(null=True)
    date_of_death = models.DateField(null=True)
    picture = models.URLField()

    def __repr__(self) -> str:
        return self.stage_name