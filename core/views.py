from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from core.models import Artist, Album, Song
from core.serializers import ArtistSerializer, AlbumSerializer, SongSerializer, RateArtistSerializer, RateAlbumSerializer, RateSongSerializer

# Create your views here.
class ArtistViewSet(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet
                   ):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = ()

    # @action(methods=['post'], detail=True, url_path='rate', )
    

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

class RatingViewSet(viewsets.GenericViewSet):
    serializer_class = None

    @action(methods=['post'], detail=True, url_path='rate')
    def rate(self, request, pk=None, *args, **kwargs):
        serializer = self.get_serializer_class()(data=request.data)
        if serializer.is_valid():
            instance = serializer.save(pk, request.user)
            return Response(instance.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArtistRatingViewSet(RatingViewSet):
    serializer_class = RateArtistSerializer

class AlbumRatingViewSet(RatingViewSet):
    serializer_class = RateAlbumSerializer

class SongRatingViewSet(RatingViewSet):
    serializer_class = RateSongSerializer
