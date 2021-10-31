from typing import List
from django.db.models.query import QuerySet
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from modules.users.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "email", "username", "password", "avatar"]
        read_only_fields = ["avatar"]
        extra_kwargs = {
            "password": {
                "write_only": True,
                "style": {"input_style": "password"}
            }
        }

    @staticmethod
    def get_queryset() -> QuerySet:
        return User.objects.all()

    def validate_password(self, value: str) -> str:
        try:
            validate_password(value)

        except ValidationError as e:
            raise serializers.ValidationError(e)

        return value

    def update(self, instance: User, validated_data: dict) -> User:
        UPDATABLE_FIELDS: List[str] = ["username"]

        update_fields: List[str] = [field for field in UPDATABLE_FIELDS if field in validated_data.keys()]

        for field in update_fields:
            setattr(instance, field, validated_data.get(field))

        instance.save(update_fields=update_fields)
        return instance


        