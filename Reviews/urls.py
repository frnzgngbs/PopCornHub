from django.urls import path
from . import views
from .views import Login

app_name = 'Reviews'
urlpatterns = [
    #path('', Login.as_view(), name='login'),
    path('review/', views.Add_Review.as_view(), name='review'),
    #path('register/', views.Register.as_view(), name='register'),
    #path('index', views.index, name='index'),
    path('display/', views.Display_Reviews.as_view(), name='display'),
]
