from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    main_genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre, related_name='other_genres')
    directors = models.ManyToManyField(Person, related_name='directed_movies')
    actors = models.ManyToManyField(Person, related_name='acted_in_movies')
    rating = models.FloatField()
    synopsis = models.TextField()
    preview_image = models.ImageField(upload_to='movie_previews/')

    def __str__(self):
        return self.title

class GalleryImage(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ImageField(upload_to='movie_gallery/')
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Image for {self.movie.title}"
class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 11)])
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.movie.title} by {self.user.username}"
