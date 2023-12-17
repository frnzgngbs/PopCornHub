from django.urls import path
from . import views
app_name = 'UserPreferences'
urlpatterns = [
    path('ViewPreferences/', views.PreferencesView.as_view(), name='ViewPreferences1'),
]