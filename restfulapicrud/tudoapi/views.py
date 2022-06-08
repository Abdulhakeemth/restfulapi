from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import User,Commodity
from rest_framework.filters import SearchFilter
from .serializers import UserSerializer,CommoditySerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from rest_framework import viewsets
from . import models
from . import serializers

class UserViewset(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    filter_backends = [SearchFilter]
    search_fields = ['user']
    permission_classes = [IsAuthenticated]


class CommodityViewset(viewsets.ModelViewSet):
    queryset = models.Commodity.objects.all()
    serializer_class = serializers.CommoditySerializer 
    filter_backends = [SearchFilter]
    search_fields = ['commodity']
    permission_classes = [IsAuthenticated]

    