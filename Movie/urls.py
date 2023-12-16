from django.urls import path
from . import views
app_name='Movie'
urlpatterns = [
    path('', views.index, name='home'),
    path('movie/', views.MovieView.as_view(), name='movie_admin'),
    path('sign/', views.SignView.as_view(), name='sign'),
    path('search/', views.movie_search, name='search'),
]