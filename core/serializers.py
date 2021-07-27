from django.core.exceptions import ValidationError
from core.models import Artist, Album, Song, ArtistRating, AlbumRating, SongRating
from rest_framework import serializers


class ArtistSerializer(serializers.ModelSerializer):
    # date_of_birth = serializers.DateField()

    class Meta:
        model = Artist
        fields = ["id", "stage_name", "real_name", "record_label", "picture", "date_of_birth", "date_of_death"]
        read_only_fields = ["rating"]

                

class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = "__all__"
        read_only_fields = ["rating"]

class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = "__all__"
        read_only_fields = ["rating"]


class RateSerializer(serializers.Serializer):
    model = None
    rate_model = None
    rate_model_name = None

    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    value = serializers.ChoiceField(choices=values)

    def save(self, object_id, user):
        obj = self.rate_model.objects.filter(id=object_id).first()
        data = {
            "value": self.validated_data['value'],
            "user": user,
            # f"{self.rate_model_name}": obj
        }
        rating = self.model.objects.create(**data)
        obj.ratings.add(rating)
        return obj

class RateArtistSerializer(RateSerializer):
    model = ArtistRating
    rate_model = Artist
    rate_model_name = "artist"

class RateAlbumSerializer(RateSerializer):
    model = AlbumRating
    rate_model = Album
    rate_model_name = "album"

class RateSongSerializer(RateSerializer):
    model = SongRating
    rate_model = Song
    rate_model_name = "song"

    # models = ['artist', 'album', 'song']
    
    # object_id = serializers.UUIDField()
    # model = serializers.ChoiceField(choices=models)
    # value = serializers.IntegerField()

    # def validate(self, data):
    #     # return super().validate(attrs)
    #     model = data.get('model')
    #     model = Artist if model == "artist" else model
    #     model = Album if model == "album" else model
    #     model = Song if model == "song" else model

    #     if isinstance(model, str):
    #         raise serializers.ValidationError("model is not one of ['artist', 'album', 'song']")
        
    #     obj = model.objects.filter(id=data.get('object_id')).first()
    #     if not obj:
    #         raise ValidationError("object_id is invalid")

    #     obj.



