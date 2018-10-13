from django.contrib import admin
from .models import Artist, Song

# Register your models here.
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('artistic_name', 'first_name', 'last_name', 'picture_url', 
        'popularity', 'genre')

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'album_name')
