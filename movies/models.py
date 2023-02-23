from django.db import models
from users.models import User

class CategoryRating(models.TextChoices):
    RATED_G = "G"
    RATED_PG = "PG"
    RATED_PG_13 = "PG-13"
    RATED_R = "R"
    RATED_NC_17 = "NC-17"

class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, default=None)
    rating = models.CharField(max_length=20, null=True, default=CategoryRating.RATED_G)
    synopsis = models.TextField(null=True, default=None)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="moveis")

class MovieOrder(models.Model):
    movie = models.ForeignKey("movies.Movie", on_delete=models.CASCADE, related_name="orders")
    user_order = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="user_movie_orders")
    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    

# Create your models here.
