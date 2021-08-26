from uuid import uuid4
from django.db import models

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

class Rating(models.Model):
    id = models.UUIDField(max_length=36, primary_key=True, editable=False, default=uuid4)
    value = models.IntegerField(choices=Ratings.choices)
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="rated")

    def __repr__(self) -> str:
        return self.value