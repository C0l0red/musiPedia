from modules.songs.models import Song
from rest_framework import serializers
from modules.artists import Artist

class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = "__all__"
        read_only_fields = ["rating"]
        extra_kwargs = {
            "featured_artists": {
                "required": False,
                "allow_empty": True
            }
        }

