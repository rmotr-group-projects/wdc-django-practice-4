from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound

from .models import Artist, Song
from .forms import ArtistForm, SongForm



def artists(request):
    # validate that user is authenticated, and if not, redirect to login page
    if not request.user.is_authenticated:
        return redirect('login')

    artists = Artist.objects.all()
    artist_form = ArtistForm()
    song_form = SongForm()

    if request.method == 'GET':
        return render(request, 'index.html', {
            'artists': artists,
            'artist_form': artist_form,
            'song_form': song_form,
        })

    if request.method == 'POST':
        artistic_name = request.POST['artistic_name']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        picture_url = request.POST['picture_url']
        popularity = request.POST['popularity']

        if not artistic_name:
            return redirect('artists')
        try:
            int(popularity)
        except ValueError:
            return redirect('artists')

        Artist.objects.create(
            artistic_name=artistic_name,
            first_name=first_name,
            last_name=last_name,
            picture_url=picture_url,
            popularity=popularity
        )

        return render(request, 'index.html', {
            'artists': artists,
            'artist_form': artist_form,
            'song_form': song_form,
            'artistic_name': artistic_name
        })


def create_song(request):
    artist_id = request.POST['artist']
    title = request.POST['title']
    album_name = request.POST.get('album_name', '')

    # validate required fields
    if not artist_id or not title:
        return redirect('artists')
    try:
        artist = Artist.objects.get(id=artist_id)
    except Artist.DoesNotExist:
        return HttpResponseNotFound()

    Song.objects.create(artist=artist, title=title, album_name=album_name)
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