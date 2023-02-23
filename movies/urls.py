from django.urls import path
from .views import MovieViews, MovieParamsViews

urlpatterns = [
    path("movies/", MovieViews.as_view()),
    path("movies/<int:movie_id>/", MovieParamsViews.as_view()),
]