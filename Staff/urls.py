from django.urls import path

from . import views

appname = 'Staff'

urlpatterns = [
    path('home/', views.AdminHome.as_view(), name="admin-home"),
    path('signout/', views.signOut, name="sign-out")
]