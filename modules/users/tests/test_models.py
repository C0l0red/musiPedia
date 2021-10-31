from factory.django import DjangoModelFactory
from rest_framework.test import APITestCase
from modules.users.models import User
from .factories import UserFactory

class TestUserModel(APITestCase):

    def setUp(self):
        factory: DjangoModelFactory = UserFactory
        self.build: User = factory.build()

    def test_user_model_saves_correctly(self):
        self.build.save()

        self.assertTrue(User.objects.filter(email=self.build.email).exists())
        