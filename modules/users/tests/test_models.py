from rest_framework.test import APITestCase
from modules.users.models import User
from .factories import UserFactory

class TestUserModel(APITestCase):

    def setUp(self):
        pass

    def test_user_model_saves_correctly(self):
        user: User = UserFactory()

        db_user: User = User.objects.first()

        self.assertEquals(db_user.username, user.username)
        