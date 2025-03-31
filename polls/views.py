from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import User, GameReview, UserGame
from .serializers import UsersGamesSerializer, GameReviewSerializer, UsersSerializer

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

# Users List and Details
class UsersListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

class UsersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

# Game Review List and Details
class GameReviewListCreate(generics.ListCreateAPIView):
    queryset = GameReview.objects.all()
    serializer_class = GameReviewSerializer

class GameReviewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = GameReview.objects.all()  # Fixed queryset
    serializer_class = GameReviewSerializer

# User Games List and Details
class UsersGamesListCreate(generics.ListCreateAPIView):
    queryset = UserGame.objects.all()
    serializer_class = UsersGamesSerializer

class UsersGamesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserGame.objects.all()
    serializer_class = UsersGamesSerializer
