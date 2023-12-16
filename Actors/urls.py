from django.urls import path
from . import views
app_name = 'Actors'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('celebs/', views.ActorsView.as_view(), name='celebs'),
]