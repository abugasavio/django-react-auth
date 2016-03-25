from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ('username',)
