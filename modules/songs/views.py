from rest_framework import viewsets, mixins, status
from rest_framework.serializers import Serializer
from rest_framework.response import Response
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

    def create(self, request, *args, **kwargs):
        data: dict = request.data

        serializer: Serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
