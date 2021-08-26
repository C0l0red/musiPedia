from modules.songs.models import Song
from rest_framework import serializers

class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = "__all__"
        read_only_fields = ["rating"]