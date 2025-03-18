from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Users, game_review, users_games
from .serializers import UsersGamesSeralizer, GameReviewSerializer, UsersSerializer
def index (request):
    return HttpResponse("Hello, world. You're at the poll index.")
# Create your views here.

#Users List and Details
class UsersListCreate(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersGamesSeralizer


class UsersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersGamesSeralizer


# Game Review List and Detail
class GameReviewListCreate(generics.ListCreateAPIView):
    queryset = game_review.objects.all()
    serializer_class = GameReviewSerializer


class GameReviewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = GameReviewSerializer


class UsersGamesListCreate(generics.ListCreateAPIView):
    queryset = users_games.objects.all()
    serializer_class = UsersGamesSeralizer

class UsersGamesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = users_games.objects.all()
    serializer_class = UsersGamesSeralizer