from django.urls import path, include
from rest_framework import generics

from movies_api.models import Movie
from movies_api.serializers.movie_serializer import MovieSerializer
from movies_api.views import MovieListView

app_name = 'movies_api'

urlpatterns = [
    path('movies/', MovieListView.as_view(), name='movie_list')
]