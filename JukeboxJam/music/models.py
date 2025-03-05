from django.db import models
from django.contrib.auth.models import User

#Defined all databases models

#playlists
class Playlist(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

#songs
class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    playlist = models.ForeignKey(
        Playlist, related_name='songs', on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.title} by {self.artist}'


