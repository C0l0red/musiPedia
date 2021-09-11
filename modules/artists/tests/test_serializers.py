from django.forms.models import model_to_dict
from modules.artists.tests.factories import ArtistFactory
from rest_framework.serializers import Serializer
from modules.artists.serializers import ArtistSerializer
from rest_framework.test import APITestCase

class TestArtistSerializer(APITestCase):

    def setUp(self):
        self.serializer = ArtistSerializer
        self.factory = ArtistFactory

    def test_serializer_is_invalid_with_no_data(self):
        serializer: Serializer = self.serializer(data={})

        self.assertFalse(serializer.is_valid())

    def test_serializer_is_valid_with_correct_data(self):
        build = self.factory.build()
        data = model_to_dict(build)

        serializer: Serializer = self.serializer(data=data)

        self.assertTrue(serializer.is_valid())