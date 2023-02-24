from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User
from django.contrib.auth.models import Group


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "is_staff",
            "groups",
        ]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["id", "name"]
