from urllib import request
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import viewsets,status
from rest_framework.decorators import api_view

from api import serializer
from .models import *
from .serializers import *


class UserView(viewsets.ViewSet):
    
    def list(self,req:Request):
        
        queryset = User.objects.all()
        serializer = UserPublic(queryset,many=True)
        
        return Response({
            'users':serializer.data
        })
        
    def create(self, req: Request):
        serializer = UserCreateSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, req: Request, pk=None):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'message': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserPublic(user)
        return Response({'user': serializer.data}, status=status.HTTP_200_OK)

    def update(self, req: Request, pk=None):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'message': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserCreateSerializer(user, data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'user': serializer.data}, status=status.HTTP_200_OK)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, req: Request, pk=None):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'message': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def partial_update(self, req: Request, pk=None):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'message': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserCreateSerializer(user, data=req.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'user': serializer.data}, status=status.HTTP_200_OK)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)