from core.models import Artist, Album, Song, RecordLabel
from rest_framework import serializers

class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = "__all__"

class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = "__all__"

class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = "__all__"

