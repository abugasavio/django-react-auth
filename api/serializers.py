from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers):
    class Meta:
        model = User
        fields = ('username',)