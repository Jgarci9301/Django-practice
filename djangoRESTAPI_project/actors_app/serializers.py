from rest_framework import serializers
from .models import Actor

class actorSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Actor
        fields = '__all__'