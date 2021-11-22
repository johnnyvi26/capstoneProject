from rest_framework import serializers
from .models import Artist, Sound

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    sounds = serializers.HyperlinkedRelatedField(
        view_name='sound_detail',
        many=True,
        read_only=True
    )
    class Meta:
       model = Artist 
       fields = ('id', 'photo_url', 'nationality', 'name', 'sounds',)

class SoundSerializer(serializers.HyperlinkedModelSerializer):
    artist = serializers.HyperlinkedRelatedField(
        view_name='artist_detail',
        # many=False,
        read_only=True
    )
    artist_id=serializers.PrimaryKeyRelatedField(
        queryset=Artist.objects.all(),
        source='artist'
    )
    class Meta:
       model = Sound 
       fields = ('id', 'artist', 'photo_url', 'title', 'album', 'photo_url', 'artist_id',)