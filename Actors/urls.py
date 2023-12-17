from django.urls import path
from . import views

app_name = 'Actors'
urlpatterns = [
    path('celebs/', views.ActorsView.as_view(), name='celebs'),
    path('update_status/', views.UpdateStatusView.as_view(), name='update_status'),
    path('add_actor_to_movie/', views.AddActorToMovieView.as_view(), name='add_actor_to_movie'),
]

