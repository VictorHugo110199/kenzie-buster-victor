from django.urls import path
from .views import MovieViews, MovieParamsViews, MovieOrderViews

urlpatterns = [
    path("movies/", MovieViews.as_view()),
    path("movies/<int:movie_id>/", MovieParamsViews.as_view()),
    path("movies/<int:movie_id>/orders/", MovieOrderViews.as_view()),
]