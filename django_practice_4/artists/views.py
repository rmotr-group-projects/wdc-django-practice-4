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
        
    elif request.method == 'POST':
        artist_form = ArtistForm(request.POST)
        song_form = SongForm(request.POST)
        
        if artist_form.is_valid():
            artistic_name = artist_form.cleaned_data['artistic_name']
            Artist.objects.create(**artist_form.cleaned_data)
            messages.success(request, 'Artist, {}, has been added!'.format(artistic_name))
            artist_form = ArtistForm()
        if song_form.is_valid():
            title = song_form.cleaned_data['title']
            Song.objects.create(**song_form.cleaned_data)
            messages.success(request, 'Song, {}, has been added!'.format(title))
            song_form = SongForm()
    
    return render(request, 'index.html', context={
        'artist_form': artist_form,
        'song_form': song_form
    })

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
