from uuid import uuid4
from django.db import models


class Song(models.Model):
    id = models.UUIDField(max_length=36, primary_key=True, editable=False, default=uuid4)
    title = models.CharField(max_length=80)
    artist = models.ForeignKey("Artist", on_delete=models.CASCADE, related_name="songs")
    featured_artist = models.ForeignKey("Artist", on_delete=models.CASCADE, related_name="features")
    album = models.ForeignKey("Album", on_delete=models.CASCADE, related_name="tracks")

    def __repr__(self) -> str:
        return self.title