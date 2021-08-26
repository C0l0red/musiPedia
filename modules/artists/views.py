from rest_framework import viewsets, mixins, status
from modules.artists.serializers import ArtistSerializer
from modules.artists.models import Artist


class ArtistViewSet(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet
                   ):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = ()