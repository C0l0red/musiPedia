from django.forms.models import model_to_dict
from django.http.response import HttpResponse
from factory.django import DjangoModelFactory
from modules.users.tests.factories import UserFactory
from django.contrib.auth.models import AbstractUser
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class TestUserListViewSet(APITestCase):

    def setUp(self) -> None:
        self.url: str = reverse("user-list")
        factory: DjangoModelFactory = UserFactory
        self.user: AbstractUser = factory.build()
        self.user_data: dict = model_to_dict(self.user, exclude=["last_login"])

    def test_post_request_with_empty_data_responds_with_a_400(self):
        response = self.client.post(self.url, data={})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_valid_data_succeeds(self):
        response = self.client.post(self.url, data=self.user_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TestUserDetailViewSet(APITestCase):

    def setUp(self) -> None:
        factory: DjangoModelFactory = UserFactory
        user: AbstractUser = factory()
        self.url: str = reverse("user-detail", kwargs={"pk": user.id})

    def test_detail_request_with_invalid_id_responds_with_a_404(self):
        url: str = reverse("user-detail", kwargs={"pk": "invalid-id"})
        response: HttpResponse = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_detail_request_with_valid_id_succeeds(self):
        response: HttpResponse = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_request_with_valid_id_succeeds(self):
        data: dict = {"username": "new_username"}

        response: HttpResponse = self.client.patch(self.url, data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_request_with_valid_id_succeeds(self):
        response: HttpResponse = self.client.delete(self.url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)