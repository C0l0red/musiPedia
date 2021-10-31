from rest_framework.test import APITestCase

from modules.songs.serializers import SongSerializer
from modules.songs import Song
from factory.django import DjangoModelFactory
from rest_framework.serializers import Serializer
from django.forms.models import model_to_dict

from modules.songs.tests.factories import SongFactory

class TestSongSerializer(APITestCase):
    
    def setUp(self):
        factory: DjangoModelFactory = SongFactory

        self.serializer_class: Serializer = SongSerializer
        self.build: Song = factory.build()

        self.build.artist.save()
        self.build.album.artist.save()
        self.build.album.save()

    def test_serializer_is_invalid_with_empty_data(self):
        data: dict = {}

        serializer: Serializer = self.serializer_class(data=data)

        self.assertFalse(serializer.is_valid())

    def test_serializer_is_valid_with_correct_data(self):
        data: dict = model_to_dict(self.build)
        data = {key:val for key,val in data.items() if val}

        serializer: Serializer = self.serializer_class(data=data)
        
        self.assertTrue(serializer.is_valid(raise_exception=True))


    