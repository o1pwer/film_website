from rest_framework import serializers

from movies_api.models import Movie, Review


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


