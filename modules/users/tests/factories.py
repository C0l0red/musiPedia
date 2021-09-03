from modules.users.models import User
import factory

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    id: str = factory.Faker("uuid4")
    username: str = factory.Faker("user_name")
    first_name: str = factory.Faker("first_name")
    last_name: str = factory.Faker("last_name")
    email: str = factory.Faker("email")
    password: str = factory.Faker("password")
    is_active: bool = True
    is_staff: bool = False
    is_superuser: bool = False

