from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound

from .models import Artist, Song
from .forms import ArtistForm, SongForm


def artists(request):
    # validate that user is authenticated, and if not, redirect to login page
    if not request.user.is_authenticated:
        return redirect('login')
        
    pass


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
