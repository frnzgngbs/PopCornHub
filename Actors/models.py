from django.db import models

from Authentication.models import User
from Movie.models import Movie


# Create your models here.
class Actors(models.Model):
    actor_id = models.CharField(max_length=20,primary_key=True, default="")
    FirstName = models.CharField(max_length=50, null=False)
    LastName = models.CharField(max_length=50, null=False)
    Age = models.IntegerField(null=False)
    BirthDate = models.DateField()
    BirthPlace = models.CharField(max_length=50, null=False)
    Height = models.FloatField()
    Description = models.TextField()
    Status = models.CharField(max_length=20, default="Active")
    Movies = models.ManyToManyField(Movie, related_name="Actors")

    def __str__(self):
        return self.FirstName + " " + self.LastName

class ActorMovie(models.Model):
    actor = models.ForeignKey(Actors, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    role = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.actor.FirstName} {self.actor.LastName} in {self.movie.MovieTitle} as {self.role}"
