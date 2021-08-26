from rest_framework import viewsets, mixins, status
from modules.albums.serializers import AlbumSerializer
from modules.albums.models import Album


class AlbumViewSet(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet
                  ):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = ()