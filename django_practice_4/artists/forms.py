from django import forms

from .models import GENRE_CHOICES, Artist


class ArtistForm(forms.Form):
    artistic_name = forms.CharField(label='Artistic Name', max_length=255)
    first_name = forms.CharField(label='First Name', max_length=255, required=False)
    last_name = forms.CharField(label='Last Name', max_length=255, required=False)
    picture_url = forms.URLField(label='URL', required=False)
    popularity = forms.IntegerField(label='Popularity', initial=0, required=False)
    genre = forms.ChoiceField(label='Genre', choices=GENRE_CHOICES, required=False)


class SongForm(forms.Form):
    artist = forms.ModelChoiceField(queryset=Artist.objects.all())
    title = forms.CharField(max_length=255)
    album_name = forms.CharField(max_length=255, required=False)
