from django.test import TestCase
from django.core.management import call_command

from artists.orm_exercises import *
from artists.models import Artist, Song


class ORMExerciesTestCase(TestCase):
    def setUp(self):
        call_command('load_initial_data')

    def test_task_1_q_object_advanced_lookup(self):
        """
            Should return all songs that contains the word 'Ground' in its
            title, OR its artist's artistic_name starts with Ed
        """
        songs = task_1_q_object_advanced_lookup()
        assert songs.count() == 2
        assert songs.filter(artist__artistic_name='Ed Sheeran').exists()
        assert songs.filter(title='Higher Ground').exists()

    def test_task_2_q_object_advanced_lookup(self):
        """
            Should return all songs that starts with the letter 'S' OR a letter 'C'
            in its title, AND its artist's artistic_name contains a letter 'W'
        """
        songs = task_2_q_object_advanced_lookup()
        assert songs.count() == 1
        assert songs[0].title == 'Superstition'
        assert songs[0].artist.artistic_name == 'Stevie Wonders'

    def test_task_3_artists_update_popularity(self):
        """Should add 10 popularity points to all artists"""
        # preconditions
        artists = Artist.objects.order_by('popularity').all()
        assert artists[0].popularity == 75
        assert artists[1].popularity == 80
        assert artists[2].popularity == 90

        task_3_artists_update_popularity()

        # postconditions
        artists = Artist.objects.order_by('popularity').all()
        assert artists[0].popularity == 85
        assert artists[1].popularity == 90
        assert artists[2].popularity == 100

    def test_task_4_songs_album_names(self):
        """Should return a list of all song's album names"""
        song_album_names = task_4_songs_album_names()
        assert list(song_album_names) == ['Divide', 'Innervisions', 'Talking book']
