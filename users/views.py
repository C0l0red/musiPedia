from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
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

    @property
    def allowed_methods(self):
        # return super().allowed_methods
        return ['GET', 'PATCH', 'DELETE']

    # def partial_update(self, request, *args, **kwargs):
    #     # return super().partial_update(request, *args, **kwargs)
    #     data = {"username": request.data}
    #     serializer = UserSerializer(data=data)
    #     if serializer.is_valid():
    #         user = serializer.save()
    #         return Response(user.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserCreateViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet
                       ):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = ()
