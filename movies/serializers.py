from rest_framework import serializers
from .models import Movie, CategoryRating, MovieOrder

class MoviesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, allow_null = True, default=None)
    rating = serializers.ChoiceField(choices = CategoryRating.choices ,default=CategoryRating.RATED_G)
    synopsis = serializers.CharField(allow_null = True, default=None)
    added_by = serializers.SerializerMethodField()

    def get_added_by(self, obj):
        return obj.user.email

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

class OrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.SerializerMethodField()
    buyed_at = serializers.DateTimeField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_by = serializers.SerializerMethodField()

    def get_title(self, obj):
        return obj.movie.title
    
    def get_buyed_by(self, obj):
        return obj.user_order.email

    def create(self, validated_data):
        return MovieOrder.objects.create(**validated_data)

