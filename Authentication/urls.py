from django.urls import path
from . import views
app_name = 'Authentication'
urlpatterns = [
    path('', views.LoginForm.as_view(), name='sign-in'),
    path('register/', views.SignUpView.as_view(), name='register'),
]