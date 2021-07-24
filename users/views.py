from rest_framework import viewsets, mixins
from users.models import User
from users.serializers import UserSerializer

# Create your views here.

class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet
                 ):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = ()

class UserCreateViewSet(mixins.CreateModelMixin,
                        viewsets.GenericViewSet
                       ):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = ()
