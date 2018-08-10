from django import forms

from .models import GENRE_CHOICES, Song, Artist


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = '__all__'
