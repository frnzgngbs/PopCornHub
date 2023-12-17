from django.shortcuts import render
from django.views import View
from django.db import connection
# Create your views here.
class PreferencesView(View):
    template_name = "preferencesView.html"

    def get(self, request):

        auth_user = request.session.get('auth')
        current_user = auth_user['username']

        with connection.cursor() as cursor:
            cursor.callproc('getUserID', [current_user])
            current_uID = cursor.fetchall()[0][0]
            cursor.close()


        args = [current_uID]

        with connection.cursor() as cursor:
            cursor.callproc('GetUserFavoriteMovies', args)
            favorite_movies = cursor.fetchall()
            cursor.close()


        with connection.cursor() as cursor:
            cursor.callproc('GetUserWatched', args)
            watched_movies = cursor.fetchall()
            cursor.close()

        with connection.cursor() as cursor:
            cursor.callproc('GetUserWatchlist', args)
            watchlist_movies = cursor.fetchall()
            cursor.close()

        return render(request, self.template_name, {"favorite_movies": favorite_movies, "watched_movies": watched_movies, "watchlist_movies":watchlist_movies})

    def post(self, request):
        auth_user = request.session.get('auth')
        current_user = auth_user['username']
        list_name = request.POST.get('list')
        movie_title = request.POST.get('movie_title')

        with connection.cursor() as cursor:
            cursor.callproc('getUserID', [current_user])
            current_uID = cursor.fetchall()[0][0]
            cursor.close()

        with connection.cursor() as cursor:
            cursor.callproc('getMovieID', [movie_title])
            movie_id = cursor.fetchall()[0][0]
            cursor.close()

        args = [current_uID, movie_id]

        if list_name == 'favorites':
            with connection.cursor() as cursor:
                cursor.callproc('RemoveMovieFromFavorites', args)
                cursor.close()
        elif list_name == 'watchlist':
            with connection.cursor() as cursor:
                cursor.callproc('RemoveMovieFromWatchList', args)
                cursor.close()

        return self.get(request)


