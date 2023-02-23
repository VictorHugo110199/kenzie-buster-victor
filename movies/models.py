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

    

# Create your models here.
