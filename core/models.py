from django.db import models
from uuid import uuid4

class Ratings(models.IntegerChoices):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5

# Create your models here.


class RecordLabel(models.Model):
    id = models.UUIDField(max_length=36, primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=120)

class Artist(models.Model):
    id = models.UUIDField(max_length=36, primary_key=True, editable=False, default=uuid4)
    real_name = models.CharField(max_length=80)
    stage_name = models.CharField(max_length=80)
    record_label = models.ForeignKey(RecordLabel, on_delete=models.CASCADE, related_name="artists")
    date_of_birth = models.DateField()
    date_of_death = models.DateField()
    picture = models.URLField()
    ratings = models.IntegerField(choices=Ratings.choices)

class Album(models.Model):
    id = models.UUIDField(max_length=36, primary_key=True, editable=False, default=uuid4)
    title = models.CharField(max_length=80)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="albums")
    release_date = models.DateField()
    cover = models.URLField()
    ratings = models.IntegerField(choices=Ratings.choices)

class Song(models.Model):
    id = models.UUIDField(max_length=36, primary_key=True, editable=False, default=uuid4)
    title = models.CharField(max_length=80)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="songs")
    featured_artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="features")
    ratings = models.IntegerField(choices=Ratings.choices)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="tracks")