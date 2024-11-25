from dataclasses import field
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from ..model.users import User
import bcrypt

class UserCreateSerializer(ModelSerializer):
    password = serializers.CharField(min_length=5, max_length=16)
    class Meta:
        model = User
        fields = ['fname','lname','username','email','password']
        
    def create(self, validated_data):
        hashed = bcrypt.hashpw(validated_data['password'].encode('utf-8'), bcrypt.gensalt())
        user = User(
            fname=validated_data['fname'],
            lname=validated_data['lname'],
            username=validated_data['username'],
            email=validated_data['email'],
            hashed_password=hashed
        )
        user.save()
        return user
        
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        field = '__all__'


class UserPublic(ModelSerializer):
    class Meta:
        model = User
        exclude = ['hashed_password']
    