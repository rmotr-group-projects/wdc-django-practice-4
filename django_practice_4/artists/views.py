from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound

from .models import Artist, Song
from .forms import ArtistForm, SongForm


def artists(request):
    # validate that user is authenticated, and if not, redirect to login page
    if not request.user.is_authenticated:
        return redirect('login')
        
    artists = Artist.objects.all()
    if request.method == 'POST':
        artist_form = ArtistForm(request.POST)
        song_form = SongForm(request.POST)

        if artist_form.is_valid():
            Artist.objects.create(**artist_form.cleaned_data)
            artist_form = ArtistForm()
        elif song_form.is_valid():
            Song.objects.create(**song_form.cleaned_data)
            song_form = SongForm()
    else:
        artist_form = ArtistForm()
        song_form = SongForm()
    return render(
        request,
        'index.html',
         context={
            'artists': artists,
            'artist_form': artist_form,
            'song_form': song_form
        }
    )


def delete_song(request):
    song_id = request.POST['song_id']
    try:
        song = Song.objects.get(id=song_id)
    except Artist.DoesNotExist:
        return HttpResponseNotFound()
    song.delete()
    return redirect('artists')


def delete_artist(request):
    artist_id = request.POST['artist_id']
    try:
        artist = Artist.objects.get(id=artist_id)
    except Artist.DoesNotExist:
        return HttpResponseNotFound()
    artist.delete()
    return redirect('artists')
