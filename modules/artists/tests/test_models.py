from modules.artists.models import Artist
from modules.artists.tests.factories import ArtistFactory
from rest_framework.test import APITestCase
from django.forms.models import model_to_dict

class TestArtistModel(APITestCase):

    def setUp(self):
        self.factory = ArtistFactory
        self.model = Artist

    def test_model_saves_correctly(self):
        build: Artist = self.factory.build()
        data: dict = model_to_dict(build)

        artist: Artist = self.model.objects.create(**data)

        self.assertTrue(self.model.objects.filter(real_name=build.real_name).exists())
