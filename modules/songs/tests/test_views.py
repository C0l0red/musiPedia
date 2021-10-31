from typing import Callable, List
from django.http.response import HttpResponse
from modules.songs.models import Song
from factory.django import DjangoModelFactory
from modules.songs.tests.factories import SongFactory
from rest_framework.test import APITestCase
from  rest_framework.reverse import reverse
from rest_framework import status
from django.forms.models import model_to_dict


class TestSongListViewSet(APITestCase):

    def setUp(self):
        factory: DjangoModelFactory = SongFactory
        self.url = reverse('song-list')
        self.build: Song = factory.build()

        self.build.artist.save()
        self.build.album.artist.save()
        self.build.album.save()

    def test_post_request_with_invalid_data_fails(self):
        response: HttpResponse = self.client.post(self.url, data={})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_valid_data_succeeds(self):
        data: dict = model_to_dict(self.build)
        data = {key:val for key,val in data.items() if val}

        response: HttpResponse = self.client.post(self.url, data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TestSongDetailViewSet(APITestCase):

    def setUp(self):
        self.factory: DjangoModelFactory = SongFactory
        self.instance: Song = self.factory()
        self.url = reverse('song-detail', kwargs={"pk": self.instance.pk})

    def test_requests_with_invalid_ids_fail(self):
        url: str = reverse('song-detail', kwargs={"pk": "invalid ID"})
        methods: List[str] = ['get', 'delete', 'patch']

        for method in methods:
            action: Callable[[str, dict], HttpResponse] = getattr(self.client, method)
            response: HttpResponse = action(url)
            
            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_detail_request_succeeds(self):
        response: HttpResponse = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_request_succeeds(self):
        data: dict = {"title": "Updated Title"}
        response: HttpResponse = self.client.patch(self.url, data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_request_succeeds(self):
        response: HttpResponse = self.client.delete(self.url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)