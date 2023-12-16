from django.forms import ModelForm, TextInput, DateField
from django import forms
from Movie.models import Movie


class MovieForm(ModelForm):
    class Meta:
        model=Movie
        fields=['MovieID', 'MovieTitle','ReleaseDate','Genre','Description', 'Rating', 'RunTime', 'Director']


from django import forms

class MovieSearchForm(forms.Form):
    SEARCH_CHOICES = [
        ('MovieID', 'Movie ID'),
        ('MovieTitle', 'Movie Title'),
        ('Genre', 'Genre'),
        ('Director', 'Director'),
        ]

    search_field = forms.ChoiceField(label='Search By', choices=SEARCH_CHOICES)
    search_query = forms.CharField(label='Search Query')

