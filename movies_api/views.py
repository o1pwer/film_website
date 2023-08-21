from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from movies_api.models import Movie
from movies_api.serializers.movie_serializer import MovieSerializer


class MovieListView(generics.ListAPIView):
    model = Movie
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer



