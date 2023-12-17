from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.db import connection

# Create your views here.
from django.views import View

class AdminHome(View):
    @method_decorator(login_required(login_url="Authentication:sign-in"))
    def get(self, request):
        context = request.session.get('trace')

        return render(request, 'admin.html', {'context': context})

    def post(self, request):
        if request.method == "POST":
            cursor = connection.cursor()
            button = request.POST.get("button")

            context = request.session.get('trace')

            if button == "user-search":
                username = request.POST.get("username")
                cursor.callproc('searchUser', [username])
                result = cursor.fetchall()
                cursor.close()

                return render(request, 'admin.html',
                              {
                                  'result': result,
                                  'type': 'user',
                                  'context': context
                              })

            elif button == "movie-search":
                selected_radio = request.POST.get('search-setting')

                setting = request.POST.get('movie')
                if selected_radio == "Movie":
                    cursor.callproc('searchByTitle', [setting])
                    result = cursor.fetchall()
                    cursor.close()
                    return render(request, 'admin.html',
                                  {
                                      'result': result,
                                      'type': 'movie',
                                      'context': context
                                  })

                elif selected_radio == "Director":
                    cursor.callproc('searchByDirector', [setting])
                    result = cursor.fetchall()
                    cursor.close()
                    return render(request, 'admin.html',
                                  {
                                      'result': result,
                                      'type': 'movie',
                                      'context': context
                                  })

                elif selected_radio == "Genre":
                    cursor.callproc('searchByGenre', [setting])
                    result = cursor.fetchall()
                    cursor.close()

                    return render(request, 'admin.html',
                                  {
                                      'result': result,
                                      'type': 'movie',
                                      'context': context
                                  })
            elif button == "review-search":
                setting = request.POST.get('review')
                cursor.callproc('searchReviewByMovieTitle', [setting])
                result = cursor.fetchall()
                cursor.close()

                return render(request, 'admin.html',
                              {
                                  'result': result,
                                  'type': 'review',
                                  'context': context
                              })

        return HttpResponse("Invalid")

def allUser(request):
    cursor = connection.cursor()
    cursor.callproc('allUser')
    result = cursor.fetchall()
    cursor.close()

    context = counter()

    return render(request, 'admin.html', {
            "result": result,
            "type": "user",
            "context": context
        })


def allMovies(request):
    cursor = connection.cursor()
    cursor.callproc('allMovies')
    result = cursor.fetchall()
    cursor.close()

    context = counter()

    return render(request, 'admin.html', {
        "result": result,
        "type": "movie",
        "context": context
    })

def allReviews(request):
    cursor = connection.cursor()
    cursor.callproc('displayReviewsMade')
    result = cursor.fetchall()
    cursor.close()

    context = counter()

    return render(request, 'admin.html', {
        "result": result,
        "type": "review",
        "context": context
    })

def deleteUser(request):
    if request.method == "POST":
        checkbox_group = request.POST.get('checkbox_group')


def signOut(request):
    logout(request)
    return redirect('Authentication:sign-in')

class Delete(View):
    def get(self, request):
        pass


    def post(self, request):
        if request.method == "POST":
            cursor = connection.cursor()
            button = request.POST.get('delete-button')

            if button == "delete-user-button":
                selectedUser = request.POST.getlist('checkbox_group')

                for pk in selectedUser:
                    new_pk = int(pk)
                    cursor.callproc('deleteUser', [new_pk])

                context = counter()

                cursor.close()
                request.session['trace'] = context

                return redirect('admin-home-users')

            elif button == "delete-movie-button":
                selectedMovies = request.POST.getlist('checkbox_group')

                for pk in selectedMovies:
                    new_pk = int(pk)
                    cursor.callproc('deleteMovie', [new_pk])

                context = counter()

                cursor.close()
                request.session['trace'] = context

                return redirect('admin-home-movies')

            elif button == "delete-review-button":
                selectedReviews = request.POST.getlist('checkbox_group')

                for pk in selectedReviews:
                    new_pk = int(pk)
                    cursor.callproc('deleteReview', [new_pk])

                context = counter()

                cursor.close()
                request.session['trace'] = context

                return redirect('admin-home-reviews')

        return redirect('admin-home-users')

def counter():
    cursor = connection.cursor()
    cursor.callproc('countUser')
    countUser = cursor.fetchall()
    user_count = countUser[0][0] if countUser else None

    # Move to the next result set
    cursor.nextset()

    # Call the 'countMovies' stored procedure
    cursor.callproc('countMovies')
    countMovie = cursor.fetchall()
    movie_count = countMovie[0][0] if countMovie else None

    cursor.nextset()

    cursor.callproc('countReviews')
    countReview = cursor.fetchall()
    review_count = countReview[0][0] if countReview else None

    context = {
        "user": user_count,
        "movie": movie_count,
        "review": review_count
    }

    return context

def spamReview(request):
    cursor = connection.cursor()
    cursor.callproc('removeSpamReview')
    result = cursor.fetchall()
    cursor.close()

    return redirect('admin-home-reviews')