from rest_framework.routers import DefaultRouter
from .albums.views import AlbumViewSet
from .artists.views import ArtistViewSet
from .songs.views import SongViewSet
from .users.views import UserViewSet

router = DefaultRouter()
router.register(r'artists', ArtistViewSet)
router.register(r'albums', AlbumViewSet)
router.register(r'songs', SongViewSet)
router.register(r'users', UserViewSet)