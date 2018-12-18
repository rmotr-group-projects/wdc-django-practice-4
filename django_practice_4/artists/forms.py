from django import forms

from .models import GENRE_CHOICES, Song, Artist


class ArtistForm(forms.Form):
    artistic_name = forms.CharField(max_length=255)
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    picture_url = forms.URLField(max_length=255)
    popularity = forms.IntegerField()
    genre = forms.ChoiceField(choices=GENRE_CHOICES)


class SongForm(forms.Form):
    artist = forms.ModelChoiceField(queryset=Artist.objects.all())
    title = forms.CharField(max_length=255)
    album_name = forms.CharField(max_length=255)

