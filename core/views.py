from rest_framework import viewsets, mixins
from core.models import Artist, Album, Song
from core.serializers import ArtistSerializer, AlbumSerializer, SongSerializer

# Create your views here.
class ArtistViewSet(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet
                   ):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = ()

class ArtistCreateViewSet(mixins.CreateModelMixin,
                          mixins.ListModelMixin,
                          viewsets.GenericViewSet
                         ):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = ()

class AlbumViewSet(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet
                  ):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = ()

class AlbumCreateViewSet(mixins.CreateModelMixin,
                          mixins.ListModelMixin,
                          viewsets.GenericViewSet
                         ):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = ()

class SongViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet
                 ):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = ()

class SongCreateViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet
                       ):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = ()