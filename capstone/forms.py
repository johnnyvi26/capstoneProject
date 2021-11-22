from django import forms
from .models import Artist, Sound

class ArtistForm(forms.ModelForm):

    class Meta:
        model = Artist
        fields = ('name', 'photo_url', 'nationality',)

class SoundForm(forms.ModelForm):

    class Meta:
        model = Sound
        fields = ('title', 'album', 'preview_url', 'artist', 'photo_url',)