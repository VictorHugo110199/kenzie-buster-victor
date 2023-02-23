from django.shortcuts import render
from rest_framework.views import APIView, Response, Request, status
from .models import Movie
from .serializers import MoviesSerializer, OrderSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from .permissions import MyCustomPermission
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from users.models import User
from kenzie_buster.pagination import CustomPageNumberPagination

class MovieViews (APIView, CustomPageNumberPagination):

    authentication_classes = [JWTAuthentication]
    permission_classes = [MyCustomPermission]
    
    
    def get (self, request):
        all_moviels = Movie.objects.all()
        result_page = self.paginate_queryset(all_moviels, request, view=self)
        serializer = MoviesSerializer(result_page, many=True)
        return self.get_paginated_response(serializer.data)

    def post (self, request):
        serializer = MoviesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class MovieParamsViews (APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [MyCustomPermission]

    def get (self, request, movie_id):
        movie = get_object_or_404(Movie, pk=movie_id)
        serializer = MoviesSerializer(movie)
        return Response(serializer.data)

    def delete (self, request, movie_id):
        movie = get_object_or_404(Movie, pk=movie_id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class MovieOrderViews (APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post (self, request, movie_id):

        movie = get_object_or_404(Movie, pk=movie_id)
        user = get_object_or_404(User, id=request.user.id)

        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(movie = movie, user_order = user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# Create your views here.
