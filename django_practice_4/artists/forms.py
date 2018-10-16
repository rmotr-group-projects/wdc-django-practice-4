from django import forms

from .models import GENRE_CHOICES, Artist


class ArtistForm(forms.Form):
    artistic_name = forms.CharField(max_length=255)
    first_name = forms.CharField(max_length=255, required=False)
    last_name = forms.CharField(max_length=255, required=False)
    picture_url = forms.URLField(max_length=255, required=False)
    popularity = forms.IntegerField(required=False)
    genre = forms.ChoiceField(choices=GENRE_CHOICES, required=False)


class SongForm(forms.Form):
    artist = forms.ModelChoiceField(queryset=Artist.objects.all())
    title = forms.CharField(max_length=255, required=False)
    album_name = forms.CharField(max_length=255, required=False)
