from django.db.models.base import Model
from django.forms.models import model_to_dict
from factory.django import DjangoModelFactory
from modules.albums.models import Album
from modules.albums.tests.factories import AlbumFactory
from rest_framework.test import APITestCase

class TestAlbumModel(APITestCase):

    def setUp(self) -> None:
        self.factory: DjangoModelFactory = AlbumFactory
        self.model: Model = Album

    def test_model_saves_correctly(self):
        build: Album = self.factory.build()
        build.artist.save()

        data: dict = model_to_dict(build, exclude="artist")
        self.model.objects.create(**data, artist=build.artist)

        self.assertTrue(self.model.objects.filter(title=build.title).exists())


