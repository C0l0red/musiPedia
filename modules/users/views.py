from modules.users.serializers import UserSerializer
from rest_framework import viewsets, mixins, status

class UserViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet
                ):
    queryset = UserSerializer.get_queryset()
    serializer_class = UserSerializer