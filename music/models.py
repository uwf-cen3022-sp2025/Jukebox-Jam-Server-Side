from django.db import models
from django.conf import settings  # Import settings

# Defined all database models

# playlists
class Playlist(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Use settings.AUTH_USER_MODEL
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# songs
class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    playlist = models.ForeignKey(
        'Playlist', related_name='songs', on_delete=models.CASCADE  # corrected string quoting.
    )

    def __str__(self):
        return f'{self.title} by {self.artist}'