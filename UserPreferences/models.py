from django.db import models
from Movie.models import Movie
from django.contrib.auth.models import User

# Create your models here.


class FavoriteMovies(models.Model):
    favoriteID = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movieID = models.ForeignKey(Movie, on_delete=models.CASCADE)
    pass


class WatchList(models.Model):
    watchlistID = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movieID = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)
    pass


class Watched(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movieID = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date_marked_as_watched = models.DateTimeField(auto_now_add=True)
    pass