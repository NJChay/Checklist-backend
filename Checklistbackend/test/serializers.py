from rest_framework import serializers
from .models import TodoItem, User


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ('id', 'title', 'completed', 'owner_id')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password')




