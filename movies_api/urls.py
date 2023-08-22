from django.urls import path
from movies_api.views import MovieListView, ReviewAddView

app_name = 'movies_api'

urlpatterns = [
    path('movies/', MovieListView.as_view(), name='movie_list'),
    path('reviews/', ReviewAddView.as_view(), name='add_review')
]