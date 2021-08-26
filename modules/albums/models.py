from uuid import uuid4
from django.db import models


class Album(models.Model):
    id = models.UUIDField(max_length=36, primary_key=True, editable=False, default=uuid4)
    title = models.CharField(max_length=80)
    artist = models.ForeignKey("Artist", on_delete=models.CASCADE, related_name="albums")
    genre  = models.CharField(max_length=50)
    release_date = models.DateField()
    cover = models.URLField()

    def __repr__(self) -> str:
        return self.title
