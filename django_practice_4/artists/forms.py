from django import forms

from .models import GENRE_CHOICES, Song, Artist


# class ArtistForm(forms.Form):
#     artistic_name = forms.CharField(max_length=255)
#     first_name = forms.CharField(max_length=255)
#     last_name = forms.CharField(max_length=255)
#     picture_url = forms.URLField()
#     popularity = forms.IntegerField(blank=True)
#     genre = forms.CharField(choices=GENRE_CHOICES, max_length=255)


# class SongForm(forms.Form):
#     artist = forms.ModelChoiceField(
#         )
#     title = forms.CharField(max_length=255)
#     album_name = forms.CharField(max_length=255)

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        exclude = []

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        exclude = []
