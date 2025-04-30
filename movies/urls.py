from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.MovieCreateListView.as_view(), name='movies'),
    path(
        'movie/<int:pk>/',
        views.MovieRetrieveUpdateDestroyView.as_view(),  name='movie'),
    path(
        'movies/stats/',
        views.MovieStatsView.as_view(), name='movie-stats-view'),
]
