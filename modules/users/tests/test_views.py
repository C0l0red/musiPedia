from django.forms.models import model_to_dict
from factory.django import DjangoModelFactory
from modules.users.tests.factories import UserFactory
from django.contrib.auth.models import AbstractUser
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class TestUserViewSet(APITestCase):

    def setUp(self) -> None:
        self.factory: DjangoModelFactory = UserFactory
        self.user: AbstractUser = self.factory.build()
        self.user_data: dict = model_to_dict(self.user, exclude=["last_login"])
        self.list_url: str = reverse("user-list")
        self.detail_url: str = reverse("user-detail", kwargs={"pk": self.user.id})

    def test_post_request_with_empty_data_responds_with_a_400(self):
        response = self.client.post(self.list_url, data={})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_valid_data_succeeds(self):
        response = self.client.post(self.list_url, data=self.user_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_detail_request_with_invalid_id_responds_with_a_404(self):
        url: str = reverse("user-detail", kwargs={"pk": "invalid-id"})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_detail_request_with_valid_id_succeeds(self):
        self.user.save()
        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_list_request_returns_all_users(self):
        user_count: int = 10
        self.factory.create_batch(user_count)

        response = self.client.get(self.list_url)

        self.assertEqual(response.data.__len__(), user_count)

    def test_patch_request_with_valid_id_succeeds(self):
        self.user.save()
        data: dict = {"username": "new_username"}

        response = self.client.patch(self.detail_url, data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_request_with_valid_id_succeeds(self):
        self.user.save()

        response = self.client.delete(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)