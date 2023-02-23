from django.shortcuts import render
from rest_framework.views import APIView, Response, Request, status
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import PermissionUser
from django.shortcuts import get_object_or_404
from .models import User
from .serializers import UserSerializer
from kenzie_buster.pagination import CustomPageNumberPagination


class UserView(APIView, CustomPageNumberPagination):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UserDetailView(APIView):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, PermissionUser]

    def get(self, req: Request, user_id):
        user = get_object_or_404(User, id=user_id)
        self.check_object_permissions(req, user)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def patch (self, req: Request, user_id):
        user = get_object_or_404(User, id=user_id)
        self.check_object_permissions(req, user)
        serializer = UserSerializer(user, req.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)




# Create your views here.
