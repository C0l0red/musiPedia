from factory.django import DjangoModelFactory
from modules.users.tests.factories import UserFactory
from django.contrib.auth.models import AbstractUser
from modules.users.serializers import UserSerializer
from unittest import TestCase
from django.forms.models import model_to_dict
from rest_framework.serializers import Serializer

class TestUserSerializer(TestCase):

    def setUp(self) -> None:
        self.serializer_class: Serializer = UserSerializer
        self.factory: DjangoModelFactory = UserFactory
        self.user: AbstractUser = self.factory.build()
        self.user_data: dict = model_to_dict(self.user)

    def test_serializer_is_invalid_with_empty_data(self):
        serializer: Serializer = self.serializer_class(data={})

        self.assertFalse(serializer.is_valid())

    def test_serializer_is_valid_with_correct_data(self):
        serializer: Serializer = self.serializer_class(data=self.user_data)

        self.assertTrue(serializer.is_valid())

    def test_serializer_is_invalid_with_weak_password(self):   
        self.user_data["password"] = "password"

        serializer: Serializer = self.serializer_class(data=self.user_data)

        self.assertFalse(serializer.is_valid())

    def test_serializer_updates_only_username(self):
        self.user.save()

        data: dict = model_to_dict(self.factory.build())
        serializer: Serializer = self.serializer_class(self.user, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        self.user.refresh_from_db()

        self.assertNotEqual(self.user.email, data.get("email"))
        self.assertEqual(self.user.username, data.get("username"))