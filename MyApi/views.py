from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class SingerView(ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class SongView(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

