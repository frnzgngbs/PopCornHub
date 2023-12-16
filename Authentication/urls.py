from django.urls import path
from . import views
app_name = 'Authentication'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register_form.as_view(), name='register'),
]