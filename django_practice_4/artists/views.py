from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from django.contrib import messages

from .models import Artist, Song
from .forms import ArtistForm, SongForm


def artists(request):
    # validate that user is authenticated, and if not, redirect to login page
    if not request.user.is_authenticated:
        return redirect('login')
        
    if request.method == 'GET':
        artist_form = ArtistForm()
        song_form = SongForm()
        return render(request, 'index.html', context={
            'artist_form': artist_form,
            'song_form': song_form
        })
        
    elif request.method == 'POST':
        if 'add_song' in request.POST:
            print('add song if')
            new_song = SongForm(request.POST)
            if new_song.is_valid():
                new_song.save()
            messages.success(request, 'Song has been added!')
            print(messages)
                
        if 'add_artist' in request.POST:
            new_artist = ArtistForm(request.POST)
            if new_artist.is_valid():
                new_artist.save()
            messages.success(request, 'Artist has been added!')
            print(messages)
                
    return redirect('artists')


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
