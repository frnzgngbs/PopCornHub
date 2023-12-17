from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .form import ReviewForm
from .form import LoginForm
from .form import RegisterForm
from django.contrib.auth.models import User
from Movie.models import Movie
from Reviews.models import Review
from django.db import connection
import logging


# Create your views here.
def index(request):
    return HttpResponse("hello world")

def add_review(request):
    # You can add any additional context data here if needed
    return render(request, 'add_review.html')

class Add_Review(View):
    template = 'add_review.html'
    logger = logging.getLogger('myapp.views.Add_Review')

    def get(self, request):
        review = ReviewForm()
        return render(request, self.template, {'form': review})

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            try:
                user_id = request.session.get('user_id')
                movie_id = 1
                #review_instance = form.save(commit=False)
                #review_instance.user_id = User.objects.get(pk=user_id)
                #review_instance.movie_id = Movie.objects.get(pk=movie_id)
                #review_instance.save()

                with connection.cursor() as cursor:
                    cursor.callproc('sp_add_review',
                                    [form.cleaned_data['rating'], form.cleaned_data['review_text'], movie_id, user_id])
                    result = cursor.fetchone()

                self.logger.info("Review created successfully")
                return redirect('Reviews:display')
            except Exception as e:
                self.logger.error(f"Error creating review: {e}")
        else:
            form_errors = form.errors.as_data()
            self.logger.error(f"Form validation errors: {form_errors}")

        return render(request, self.template, {'form': form})


class Login(View):
    logger = logging.getLogger('myapp.views.Login')

    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            try:
                user = User.objects.get(username=username)

                if user.password == password:
                    request.session['user_id'] = user.userID
                    self.logger.info("Successful login")
                    return redirect('Reviews:review')
                else:
                    self.logger.info("Unsuccessful login")
            except User.DoesNotExist:
                self.logger.info("Unsuccessful login")

        form = LoginForm()
        return render(request, 'login.html', {'form': form})


class Register(View):
    template = 'register.html'
    logger = logging.getLogger('myapp.views.Register')

    def get(self, request):
        form = RegisterForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            self.logger.info("Registration successful")
            return redirect('Reviews:login')
        else:
            self.logger.error("Registration failed. Please check the provided information.")

        return render(request, self.template, {'form': form})

class Display_Reviews(View):
    template = 'display_reviews.html'
    logger = logging.getLogger('myapp.views.Display_Reviews')

    def get(self, request):
        try:
            if 'user_id' in request.session:
                user_id = request.session['user_id']
                user_reviews = Review.objects.filter(user_id=user_id)
                return render(request, self.template, {'reviews': user_reviews})
            else:
                return render(request, 'login.html')
        except Exception as e:
            self.logger.error(f"Error retrieving reviews: {e}")
            reviews = []
        return render(request, self.template, {'reviews': reviews})
