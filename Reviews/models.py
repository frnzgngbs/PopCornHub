from django.db import models
from django.utils import timezone
# import models from other apps
from django.contrib.auth.models import User
from Movie.models import Movie
# Create your models here.


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    rating = models.IntegerField()
    review_text = models.TextField()
    review_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)
