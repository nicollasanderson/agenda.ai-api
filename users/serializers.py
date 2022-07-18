from dataclasses import fields
from rest_framework import serializers
from django.utils import timezone

from users.models import User


class UserReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name", "img"]


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "password",
            "is_professor",
            "img",
        ]
        read_only_fields = ["updated_at", "id"]

    def create(self, validated_data):

        validated_data["date_joined"] = timezone.now()
        validated_data["username"] = validated_data["email"]

        user = User.objects.create(**validated_data)

        user.set_password(validated_data["password"])

        user.save()

        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]
