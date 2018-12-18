from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound

from .models import Artist, Song
from .forms import ArtistForm, SongForm


def artists(request):
    # validate that user is authenticated, and if not, redirect to login page
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method == 'GET':
        artist_form = ArtistForm()
        song_form = SongForm()
        
    if request.method == 'POST':    
        artist_form = ArtistForm(request.POST)
        song_form = SongForm(request.POST)
        if song_form.is_valid():
            Song.objects.create(**song_form.cleaned_data)
            song_form = SongForm()
        
    artists = Artist.objects.all()
  
    return render(request, 'index.html', {
        'artists': artists,
        'artist_form': artist_form,
        'song_form' : song_form
    })

def create_artist(request):
    artist_form = ArtistForm(request.POST)

    if artist_form.is_valid():
        artistic_name = artist_form.cleaned_data['artistic_name']
        first_name = artist_form.cleaned_data['first_name']
        last_name = artist_form.cleaned_data['last_name']
        picture_url = artist_form.cleaned_data['picture_url']
        popularity = artist_form.cleaned_data['popularity']
        genre = artist_form.cleaned_data['genre']
        
    if not artistic_name:
        return redirect('artists')
        
    Artist.objects.create(
        artistic_name=artistic_name,
        first_name=first_name,
        last_name=last_name,
        picture_url=picture_url,
        popularity=int(popularity),
        genre=genre)
        
    return redirect('artists')
    

# def create_song(request):
#     song_form=SongForm(request.POST)
    
#     if song_form.is_valid():
#         title = song_form.cleaned_data['title']
#         album_name = song_form.cleaned_data['album_name']
#         artist = song_form.cleaned_data['artist']

#     if not artist or not title:
#         return redirect('artists')
    
#     Song.objects.create(
#         artist=artist,
#         title=title,
#         album_name=album_name)
        
#     return redirect('artists')

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
