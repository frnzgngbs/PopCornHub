from django.contrib.auth import login, authenticate, logout
from django.db import connection
from django.shortcuts import redirect, render
from django.views import View

from Authentication.form import SignUpForm


class SignUpView(View):
    template_name = "registration.html"

    def get(self, request):
        form = SignUpForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Authentication:sign-in')

        return render(request, self.template_name, {"form": form})


class LoginForm(View):
    template_name = "sign-in.html"
    def get(self, request):
        if request.user.is_authenticated:
            if request.user.is_staff:
                return redirect('admin-home')
            return redirect('Movie:search')
        return render(request, self.template_name)

    def post(self, request):
        if request.method == "POST":

            uname = request.POST.get("username")
            passw = request.POST.get("password")

            auth = {
                "username": uname,
                "password": passw
            }

            user = authenticate(request, username=uname, password=passw)

            if user is not None:
                print(user.is_staff)
                if user.is_staff:
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

                    request.session['trace'] = context

                    login(request, user)
                    request.session['auth'] = auth
                    return redirect('admin-home')
                else:
                    login(request, user)
                    request.session['auth'] = auth
                    return redirect('Authentication:register')

        return redirect('Authentication:sign-in')


