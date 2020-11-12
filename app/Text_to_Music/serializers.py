from rest_framework import serializers
from .models import ReturnMusicFile

class MusicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ReturnMusicFile
        fields = ['music', 'picture']