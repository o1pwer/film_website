from django.urls import path

from movies_api import func_views
from movies_api.class_views import MovieListAPIView, ReviewAddView, MovieSearchAPIView, MovieDetailAPIView

app_name = 'movies_api'

urlpatterns = [
    path('movies/', MovieListAPIView.as_view(), name='movie_list'),
    path('movies/search/', MovieSearchAPIView.as_view(), name='movie_search'),
    path('movies/<slug:genre>/<int:film_id>/', MovieDetailAPIView.as_view(), name='movie_detail'),
    path('reviews/', ReviewAddView.as_view(), name='add_review'),
    path('login/', func_views.obtain_auth_token, name='login'),
    path('logout/', func_views.logout, name='logout'),
    path('register/', func_views.register, name='register'),
]
