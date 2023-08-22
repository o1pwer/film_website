from django.db.models import Q
from django.http import HttpResponse
# Create your views here.
from rest_framework import generics

from movies_api.models import Movie, Review
from movies_api.serializers.movie_serializers import MovieSerializer
from movies_api.serializers.review_serializers import ReviewSerializer


class MovieListView(generics.ListAPIView):
    model = Movie
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        filter_params = self.request.GET.dict()

        # Apply filters dynamically
        queryset, order_by_param = self.apply_filters(queryset, filter_params)

        # Apply order-by dynamically
        if order_by_param:
            queryset = self.apply_ordering(queryset, order_by_param)

        return queryset

    def apply_filters(self, queryset, filter_params):
        q_objects = Q()
        # Handle required directors
        if directors_required := filter_params.pop('directors_required', None):
            required_director_ids = directors_required.split(',')
            for director_id in required_director_ids:
                q_objects &= Q(directors__id=director_id)

        # Handle optional directors
        if directors_optional := filter_params.pop('directors_optional', None):
            optional_director_ids = directors_optional.split(',')
            q_objects &= (Q(directors__id__in=optional_director_ids) | Q(directors=None))
        # Handle required actors
        if actors_required := filter_params.pop('actors_required', None):
            required_actor_ids = actors_required.split(',')
            for actor_id in required_actor_ids:
                q_objects &= Q(actors__id=actor_id)

        # Handle optional actors
        if actors_optional := filter_params.pop('actors_optional', None):
            optional_actor_ids = actors_optional.split(',')
            q_objects &= (Q(actors__id__in=optional_actor_ids) | Q(actors=None))

        if rating_range := filter_params.pop('rating_range', None):
            min_rating, max_rating = rating_range.split(',')
            q_objects &= Q(rating__gte=min_rating, rating__lte=max_rating)

        # Remove 'order_by' from filter_params
        order_by_param = filter_params.pop('order_by', None)

        q_objects &= Q(**filter_params)
        queryset = queryset.filter(q_objects)

        return queryset, order_by_param

    def apply_ordering(self, queryset, order_by_params):
        # Validate and sanitize order-by fields
        valid_fields = [field.name for field in Movie._meta.fields]
        sanitized_order_by = [field for field in order_by_params if field.lstrip('-') in valid_fields]

        return queryset.order_by(*sanitized_order_by)


class ReviewAddView(generics.CreateAPIView):
    model = Review
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return HttpResponse(status=201)
