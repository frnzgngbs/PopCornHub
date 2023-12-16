
from django.views import View
from django.shortcuts import render, redirect
from .form import MovieForm
from django.db import connection
from django.shortcuts import render
from django.http import HttpResponse
from .form import MovieSearchForm
from .models import Movie
# Create your views here.

def display_movie_details(request, movie):
    return render(request, 'MovieDetails.html', {'movie': movie})

from django.db.models import Q

def movie_search(request):
    if request.method == 'POST':
        form = MovieSearchForm(request.POST)
        if form.is_valid():
            search_field = form.cleaned_data['search_field']
            search_query = form.cleaned_data['search_query']

            # Create a dictionary to map form field names to model field names
            field_mapping = {
                'MovieID': 'MovieID',
                'MovieTitle': 'MovieTitle',
                'Genre': 'Genre',
                'Director': 'Director',
                # Add other fields here
            }

            # Get the model field name based on user's selection
            model_field = field_mapping.get(search_field)

            if model_field:
                # Construct the query dynamically based on user's selection
                movies = Movie.objects.filter(**{model_field: search_query})

                if movies.exists():
                    return render(request, 'Search.html', {'form': form, 'movies': movies})
                else:
                    error_message = f"No movies found with {search_field} equal to '{search_query}'."
                    return render(request, 'Search.html', {'form': form, 'error_message': error_message})
    else:
        form = MovieSearchForm()
    return render(request, 'Search.html', {'form': form})


def index(request):
    return HttpResponse("hello world")

class MovieView(View):
    template_name = 'erwin.html'  # Corrected template_name

    def get(self, request):
        movie_form = Movie.objects.all() # Create an instance of MovieForm
        return render(request, self.template_name, {'movies': movie_form, 'form': MovieForm()})

    def post(self, request):
        movie_form = MovieForm(request.POST)  # Bind the form data
        movieID = request.POST['MovieID']
        movieTitle = request.POST['MovieTitle']
        releaseDate = request.POST['ReleaseDate']
        genre = request.POST['Genre']
        description = request.POST['Description']
        runtime = request.POST['RunTime']
        director = request.POST['Director']
        result = ""
        if movie_form.is_valid():
            cursor = connection.cursor()
            args = [movieID, movieTitle, releaseDate, genre, description, runtime, director];
            cursor.callproc('AddMovie', args)
            result = cursor.fetchall()
            cursor.close()
            return redirect('admin:Movie_movie_changelist')  # Redirect to the admin Movie change list
        return render(request, self.template_name, {'form': movie_form})

class SignView(View):
    templates = 'Signup.html'

    def get(self, request):
        sign = MovieForm()
        return render(request, self.templates)

class Login2View(View):
    templates = 'Login2.html'

    def get(self, request):
        log = MovieForm()
        return render(request, self.templates)
