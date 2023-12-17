from multiprocessing import connection
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse

from Movie.models import Movie
from .form import ActorsForm
from django.http import HttpResponse
from django.views import View
from django.db import connection
from django.views.generic import View
from django.shortcuts import render, get_object_or_404
from .models import Actors, ActorMovie
from .models import Actors
from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.http import require_POST
from .models import Actors
from django.views.decorators.http import require_POST

# Create your views here.
def login(request):
    return render(request, 'sign-in.html')

class AddActorToMovieView(View):
    template_name = 'add_actor_to_movie.html'

    def get(self, request):
        # You can add any logic needed for GET requests
        return render(request, self.template_name)

    def post(self, request):
        actor_id = request.POST.get('actor_id')
        movie_id = request.POST.get('movie_id')
        role = request.POST.get('role')

        # Check if both actor and movie exist before creating ActorMovie instance
        try:
            actor = Actors.objects.get(actor_id=actor_id)
            movie = Movie.objects.get(MovieID=movie_id)
        except (Actors.DoesNotExist, Movie.DoesNotExist):
            # Handle the case where either actor or movie doesn't exist
            # You might want to display an error message or redirect to an error page
            return render(request, self.template_name, {'error': 'Actor or Movie not found'})

        # Create an ActorMovie instance
        actor_movie = ActorMovie.objects.create(actor=actor, movie=movie, role=role)

        # Redirect to the movie details or any other page
        return render(request, self.template_name)
class UpdateStatusView(View):
    template_name = 'update_status.html'

    def get(self, request):
        # Add any necessary logic for handling GET requests (optional)
        return render(request, self.template_name)

    def post(self, request):
        actor_id = request.POST.get('actor_id')
        status = request.POST.get('status')

        # Update actor status in the database
        actor = Actors.objects.get(actor_id=actor_id)
        actor.Status = status
        actor.save()

        # Redirect to the update_status.html template
        return render(request, self.template_name)

class ActorsView(View):
    template_name = 'celebs.html'

    def get(self, request):
        form = ActorsForm()
        actors = Actors.objects.all()  # Retrieve all actors from the database
        return render(request, 'celebs.html', {'form': form, 'actors': actors})

    def post(self, request):
        form = ActorsForm(request.POST)
        if form.is_valid():
            actor_id = request.POST.get('actor_id')
            firstname = request.POST.get('FirstName')
            lastname = request.POST.get('LastName')
            age = request.POST.get('Age')
            birthday = request.POST.get('BirthDate')
            birthplace = request.POST.get('BirthPlace')
            height = request.POST.get('Height')
            description = request.POST.get('Description')
            status = request.POST.get('Status')

            args = [actor_id, firstname, lastname, age, birthday, birthplace, height, description, status]
            cursor = connection.cursor()
            cursor.callproc('InsertActor', args)
            result = cursor.fetchall()

        # Retrieve all actors from the database and update the context
        actors = Actors.objects.all()
        return render(request, 'celebs.html', {'form': form, 'actors': actors})
