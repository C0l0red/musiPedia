from modules.songs.models import Song
import factory

class SongFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Song
        # exclude = ["featured_artist"]

    id = factory.Faker("uuid4")
    title = factory.Faker("word")
    artist = factory.SubFactory("modules.artists.ArtistFactory")
    # featured_artist = factory.SubFactory("modules.artists.ArtistFactory")
    # featured_arists = factory.LazyAttribute(lambda o: [])
    album = factory.SubFactory("modules.albums.AlbumFactory")
    