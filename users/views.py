from django.shortcuts import render
from rest_framework.views import APIView, Response, Request, status
from .serializers import UserSerializer


class UserView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# Create your views here.
