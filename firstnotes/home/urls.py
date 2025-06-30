from django.urls import path

from . import views
urlpatterns = [
    path('home', views.home, name='home'),
    path('authorized', views.authorized, name='authorized'),
    # You can add more URL patterns here as needed
]