from rest_framework.test import APITestCase
from factory.django import DjangoModelFactory
from modules.songs import SongFactory
from modules.songs.models import Song

class TestSongModel(APITestCase):

    def setUp(self):
        factory: DjangoModelFactory = SongFactory
        self.build: Song = factory.build()

        self.build.artist.save()
        self.build.album.artist.save()
        self.build.album.save()

    def test_model_saves_correctly(self):
        self.build.save()

        self.assertTrue(Song.objects.filter(title=self.build.title).exists())