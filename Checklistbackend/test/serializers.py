from rest_framework import serializers
from .models import TodoItem


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ('id', 'title', 'completed', 'owner_id')
