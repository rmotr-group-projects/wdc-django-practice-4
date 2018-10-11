from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound

from .models import Artist, Song
from .forms import ArtistForm, SongForm


def artists(request):
    # validate that user is authenticated, and if not, redirect to login page
    if not request.user.is_authenticated:
        return redirect('login')

    # If it is a 'POST' request, make an instance of the form with the data
    # provided and, if it is valid, create the Artist object
    if request.method == 'POST':
        add_artist_form = ArtistForm(request.POST)
        if add_artist_form.is_valid():
            Artist.objects.create(
                artistic_name=add_artist_form.cleaned_data['artistic_name'],
                first_name=add_artist_form.cleaned_data['first_name'],
                last_name=add_artist_form.cleaned_data['last_name'],
                picture_url=add_artist_form.cleaned_data['picture_url'],
                popularity=add_artist_form.cleaned_data['popularity'],
                genre=add_artist_form.cleaned_data['genre'])
        return redirect('artists')
    # For a GET (or any other method), make an instance of the form and return it,
    # as well as a query set containing all artists, to the template as context
    else:
        add_artist_form = ArtistForm()
        artists = Artist.objects.all()
        return render(request, 'index.html', 
            {'add_artist_form': add_artist_form, 'artists': artists})


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
