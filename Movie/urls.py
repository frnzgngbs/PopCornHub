from django.urls import path
from . import views
app_name = 'Movie'
urlpatterns = [
    path('movie/', views.MovieView.as_view(), name='movie_admin'),
    path('search/', views.movie_search, name='search'),
    path('signout/', views.SignOutView.as_view(), name='signout'),
    path('dispaly/', views.displayDetails, name='displayDetails')
]