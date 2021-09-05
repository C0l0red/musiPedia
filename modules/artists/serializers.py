from modules.artists.models import Artist
from rest_framework import serializers

class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ["id", "stage_name", "real_name", "record_label", "picture", "date_of_birth", "date_of_death"]
        read_only_fields = ["rating"]