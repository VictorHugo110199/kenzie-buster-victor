from django.urls import path
from .views import UserView, UserDetailView
from rest_framework_simplejwt import views 

urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/login/", views.TokenObtainPairView.as_view()),
    path("users/<int:user_id>/", UserDetailView.as_view()),
]