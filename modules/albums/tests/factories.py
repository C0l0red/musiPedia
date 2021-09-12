from modules.albums.models import Album
import factory 

class AlbumFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Album

    id = factory.Faker("uuid4")
    title = factory.Faker("word")
    artist = factory.SubFactory("modules.artists.ArtistFactory")
    genre = factory.Faker("word")
    release_date = factory.Faker("past_date")
    cover = factory.Faker("image_url")