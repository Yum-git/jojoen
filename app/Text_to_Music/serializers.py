from rest_framework import serializers
from .models import ReturnMusicFile

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReturnMusicFile
        fields = ['music', 'picture']