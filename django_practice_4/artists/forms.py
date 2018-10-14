from django import forms
from .models import Artist, Song
from .models import GENRE_CHOICES, Song


class ArtistForm(forms.Form):
    artistic_name = forms.CharField(label='Artist Name', max_length=100)
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    picture_url = forms.URLField(label='Picture url', max_length=100)
    popularity = forms.IntegerField(label='Popularity')
    genre = forms.CharField(label='Genre', max_length=100)


class SongForm(forms.Form):
    artist = forms.ModelChoiceField(queryset=Artist.objects.all())
    title = forms.CharField(label='Title', max_length=100)
    album_name = forms.CharField(label='Album Name', max_length=100)
