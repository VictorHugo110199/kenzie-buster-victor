from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(
        max_length=150,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), message="username already taken."
            )
        ],
    )
    email = serializers.EmailField(
        max_length=127,  
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), message="email already registered."
            )
        ],
    )
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birthdate =  serializers.DateField(default = True)
    is_employee = serializers.BooleanField(default=False)
    password = serializers.CharField(max_length = 100, write_only=True)
    is_superuser = serializers.BooleanField(read_only=True)


    def create(self, validated_data):
        if validated_data['is_employee'] is True:
            return User.objects.create_user(**validated_data, is_superuser=True)
        return User.objects.create_user(**validated_data)
    
    




