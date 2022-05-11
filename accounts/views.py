from django.shortcuts import render
from rest_framework import viewsets

from .models import User
from .serializers import CustomUserSlz

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = CustomUserSlz
    queryset = User.objects.all()
