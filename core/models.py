from re import S
from django.db import models
from uuid import uuid4
from users.models import User
from django.db.models import Avg
from django.contrib.postgres.fields import ArrayField

class Ratings(models.IntegerChoices):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10

# Create your models here.

class RatingMixin:
    @property
    def rating(self):
        self.ratings.all().aggregate(Avg('value'))

class Artist(models.Model, RatingMixin):
    id = models.UUIDField(max_length=36, primary_key=True, editable=False, default=uuid4)
    real_name = models.CharField(max_length=80)
    stage_name = models.CharField(max_length=80, unique=True)
    # record_labels = ArrayField(models.CharField(max_length=120))
    record_label = models.CharField(max_length=120)
    date_of_birth = models.DateField(null=True)
    date_of_death = models.DateField(null=True)
    picture = models.URLField()

    def __repr__(self) -> str:
        return self.stage_name

class Album(models.Model, RatingMixin):
    id = models.UUIDField(max_length=36, primary_key=True, editable=False, default=uuid4)
    title = models.CharField(max_length=80)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="albums")
    genre  = models.CharField(max_length=50)
    release_date = models.DateField()
    cover = models.URLField()

    def __repr__(self) -> str:
        return self.title


class Song(models.Model, RatingMixin):
    id = models.UUIDField(max_length=36, primary_key=True, editable=False, default=uuid4)
    title = models.CharField(max_length=80)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="songs")
    featured_artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="features")
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="tracks")

    def __repr__(self) -> str:
        return self.title

class Rating(models.Model):
    id = models.UUIDField(max_length=36, primary_key=True, editable=False, default=uuid4)
    value = models.IntegerField(choices=Ratings.choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rated")

    def __repr__(self) -> str:
        return self.value

class ArtistRating(Rating):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="ratings")

class AlbumRating(Rating):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="ratings")

class SongRating(Rating):
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="ratings")