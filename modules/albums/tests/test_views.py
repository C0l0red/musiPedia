from typing import List
from django.forms.models import model_to_dict
from modules.albums.tests.factories import AlbumFactory
from factory.django import DjangoModelFactory
from modules.albums.models import Album
from django.db.models.base import Model
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status

class TestAlbumListViewSet(APITestCase):

    def setUp(self):
        self.url = reverse('album-list')
        self.model: Model = Album
        self.factory: DjangoModelFactory = AlbumFactory

    def test_post_request_with_invalid_data_fails(self):
        response = self.client.post(self.url, data={})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_valid_data_succeeds(self):
        build: Album = self.factory.build()
        build.artist.save()

        data: dict = model_to_dict(build)
        response = self.client.post(self.url, data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_list_request_returns_list(self):
        response = self.client.get(self.url)

        self.assertIsInstance(response.data, list)

    def test_get_list_request_succeeds(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestAlbumDetailViewSet(APITestCase):
    
    def setUp(self):
        self.factory: DjangoModelFactory = AlbumFactory
        instance: Album = self.factory()
        self.url: str = reverse('album-detail', kwargs={"pk": instance.pk})

    def test_requests_fail_with_bad_id(self):
        methods: List[str] = ["get", "patch", "delete"]
        url: str = reverse('album-detail', kwargs={"pk": "Wrong uid"})

        for method_name in methods:
            method = getattr(self.client, method_name)
            response = method(url)

            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_detail_request_succeeds(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_request_succeeds(self):
        build: Album = self.factory.build()
        data: dict = model_to_dict(build, fields="title")

        response = self.client.patch(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_request_succeeds(self):
        response = self.client.delete(self.url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)