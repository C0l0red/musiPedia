from modules.albums.models import Album
from rest_framework import serializers

class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = "__all__"
        read_only_fields = ["rating"]