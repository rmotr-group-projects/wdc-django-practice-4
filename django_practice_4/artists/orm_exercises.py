from django.db.models import Q, F

from artists.models import Artist, Song


def task_1_q_object_advanced_lookup():
    """
        Should return all songs that contains the word 'Ground' in its
        title, OR its artist's artistic_name starts with Ed
    """
    # HINT: Use django Q object to allow "OR" expresions in .filter()
    return Song.objects.filter(
        Q(title__icontains='Ground') |
        Q(artist__artistic_name__startswith='Ed')
    )


def task_2_q_object_advanced_lookup():
    """
        Should return all songs that starts with the letter 'S' OR a letter 'C'
        in its title, AND its artist's artistic_name contains a letter 'W'
    """
    # HINT: Use django Q object to allow "OR" and "AND" expresions combined.
    # Avoid using .filter() multiple times.
    return Song.objects.filter(
        (
            Q(title__startswith='S') |
            Q(title__startswith='C')
        )
        & Q(artist__artistic_name__icontains='W')
    )


def task_3_artists_update_popularity():
    """Should add 10 popularity points to all artists"""
    # HINT: Use .update() function and django F object to refer to model's fields values
    Artist.objects.update(popularity=F('popularity') + 10)


def task_4_songs_album_names():
    """Should return a list of all song's album names ordered alphabetically"""
    # HINT: Use .values_list() function with 'flat' option, to get from the
    # database only the fields that you are interested in and not all the ones
    # in the model
    return Song.objects.order_by(
        'album_name'
    ).values_list(
        'album_name', flat=True
    ).all()
