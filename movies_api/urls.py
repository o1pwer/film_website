from django.urls import path
from movies_api.views import MovieListAPIView, ReviewAddView, MovieSearchAPIView, MovieDetailAPIView

app_name = 'movies_api'

urlpatterns = [
    path('movies/', MovieListAPIView.as_view(), name='movie_list'),
    path('movies/search/', MovieSearchAPIView.as_view(), name='movie_search'),
    path('movies/<slug:genre>/<int:film_id>/', MovieDetailAPIView.as_view(), name='movie_detail'),
    path('reviews/', ReviewAddView.as_view(), name='add_review')
]