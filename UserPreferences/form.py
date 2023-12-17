from django import forms
from .models import *


class FavoriteMoviesForm(forms.ModelForm):

    class Meta:
        model = FavoriteMovies
        fields=['user',  'movieID']


class WatchListForm(forms.ModelForm):

    class Meta:
        model = WatchList
        fields=['user', 'movieID']


class WatchedForm(forms.ModelForm):

    class Meta:
        model = Watched
        fields=['user', 'movieID']