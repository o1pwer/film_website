from rest_framework import serializers

from movies_api.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'  # Include all fields from the Movie model