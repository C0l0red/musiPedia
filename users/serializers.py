from users.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={"input_type": "password"})
    class Meta:
        model = User
        fields = ["id", "email", "username", "password", "image"]
        # extra_kwargs = {"password": {"write_only": True}}
        read_only_fields = ["image"]


    def create(self, validated_data):
        print(validated_data)

        password = validated_data["password"]
        hashed_password = make_password(password)
        
        validated_data["password"] = hashed_password

        user = User(**validated_data)
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.username)
        instance.save()
        return instance
        