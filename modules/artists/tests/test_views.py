from typing import List
from modules.artists.tests.factories import ArtistFactory
from factory.django import DjangoModelFactory
from modules.artists.models import Artist
from django.forms.models import model_to_dict
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status

class TestArtistListViewSet(APITestCase):

    def setUp(self):
        self.url = reverse('artist-list')
        self.model: Artist = Artist
        self.factory: DjangoModelFactory = ArtistFactory

    def test_post_request_with_invalid_data_fails(self):
        response = self.client.post(self.url, data={})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_valid_data_succeeds(self):
        build: Artist = self.factory.build()
        data: dict = model_to_dict(build)
        response = self.client.post(self.url, data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_list_request_returns_list(self):
        response = self.client.get(self.url)

        self.assertIsInstance(response.data, list)

    def test_get_list_request_succeeds(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

class TestArtistDetailViewSet(APITestCase):
    
    def setUp(self):
        self.factory: DjangoModelFactory = ArtistFactory
        instance: Artist = self.factory()
        self.url = reverse('artist-detail', kwargs={"pk": instance.id})
        

    def test_requests_fail_with_bad_id(self):
        methods: List[str] = ['get', 'patch', 'delete']
        url = reverse('artist-detail', kwargs={"pk": "invalid id"})

        for method_name in methods:
            method = getattr(self.client, method_name)
            response = method(url)
            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_detail_request_succeeds(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_patch_request_succeeds(self):
        build = self.factory.build()
        data: dict = model_to_dict(build)
        response = self.client.patch(self.url, data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_request_succeeds(self):
        response = self.client.delete(self.url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
