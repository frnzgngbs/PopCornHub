from django.urls import path

from . import views

appname = 'Staff'

urlpatterns = [
    path('home/', views.AdminHome.as_view(), name="admin-home"),
    path('home/users', views.allUser, name="admin-home-users"),
    path('home/movies', views.allMovies, name="admin-home-movies"),
    path('home/movies/reviews', views.allReviews, name="admin-home-reviews"),
    path('home/movies/spam-reviews', views.spamReview, name="admin-home-spam-reviews"),
    path('signout/', views.signOut, name="sign-out"),
    path('home/delete', views.Delete.as_view(), name="delete")
]