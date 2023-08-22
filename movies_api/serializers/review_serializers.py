from rest_framework import serializers

from movies_api.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        extra_kwargs = {
            'movie': {'required': True},
            'user': {'required': True},
            'rating': {'required': True},
            'text': {'required': True},
        }