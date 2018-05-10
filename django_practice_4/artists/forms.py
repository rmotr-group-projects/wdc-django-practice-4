from django import forms

from .models import GENRE_CHOICES, Song


class ArtistForm(forms.Form):
    artistic_name = forms.CharField(label='Artistic name', max_length=200)
    first_name = forms.CharField(label='First name', max_length=200, required=False)
    last_name = forms.CharField(label='Last name', max_length=200, required=False)
    picture_url = forms.URLField(label='Picture URL', required=False)
    popularity = forms.IntegerField(label='Popularity', min_value=0, max_value=100, required=False)
    genre = forms.ChoiceField(label='Genre', choices=GENRE_CHOICES, required=False)


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['artist', 'title', 'album_name']
