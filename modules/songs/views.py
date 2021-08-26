from rest_framework import viewsets, mixins, status
from modules.songs.serializers import SongSerializer
from modules.songs.models import Song


class SongViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet
                 ):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = ()