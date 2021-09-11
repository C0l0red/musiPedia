from modules.artists.models import Artist
import factory

class ArtistFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Artist

    id = factory.Faker("uuid4")
    real_name = factory.Faker("name")
    stage_name = factory.Faker("first_name")
    record_label = factory.Faker("company")
    date_of_birth = factory.Faker("date_of_birth")
    date_of_death = factory.Faker("date_this_year")
    picture = factory.Faker("image_url")