from django.contrib import admin

# Register your models here.
from movies.models import Movie
from actors.models import Actor


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'genre', 'release_date')