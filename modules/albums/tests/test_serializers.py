from django.forms.models import model_to_dict
from modules.albums.models import Album
from modules.albums.tests.factories import AlbumFactory
from factory.django import DjangoModelFactory
from modules.albums.serializers import AlbumSerializer
from rest_framework.test import APITestCase
from rest_framework.serializers import Serializer

class TestAlbumSerializer(APITestCase):

    def setUp(self):
        self.serializer: Serializer = AlbumSerializer
        self.factory: DjangoModelFactory = AlbumFactory

    def test_serializer_is_invalid_with_empty_data(self):
        serializer: Serializer = self.serializer(data={})

        self.assertFalse(serializer.is_valid())

    def test_serializer_is_valid_with_correct_data(self):
        build: Album = self.factory.build()
        build.artist.save()
        
        data: dict = model_to_dict(build)
        serializer: Serializer = self.serializer(data=data)

        self.assertTrue(serializer.is_valid())
