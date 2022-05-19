from django.db import models
from django.conf import settings

class Genre(models.Model):
    # genre_id = models.IntegerField(unique=True)
    genre_name = models.CharField(max_length=50)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_genres')
    
    def __str__(self):
        return self.genre_name

class Movie(models.Model):
    movie_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=100)
    released_date = models.DateField()
    popularity = models.FloatField()
    vote_avg = models.DecimalField(max_digits=4, decimal_places=2)
    overview = models.TextField(null=True)
    poster_path = models.CharField(max_length=200, null=True)
    genres = models.ManyToManyField(Genre, related_name='movies', blank=True)
    actors = models.JSONField(null=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

