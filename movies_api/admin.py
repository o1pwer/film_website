from django.contrib import admin

# Register your models here.
from movies_api.models import Movie, Person, Genre


class MovieAdmin(admin.ModelAdmin):
    pass

admin.site.register(Movie, MovieAdmin)

class PersonAdmin(admin.ModelAdmin):
    pass

admin.site.register(Person, PersonAdmin)

class GenresAdmin(admin.ModelAdmin):
    pass

admin.site.register(Genre, GenresAdmin)