from rest_framework import serializers
from .models import Users, game_review, users_games

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class GameReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = game_review
        fields = '__all__'

class UsersGamesSeralizer(serializers.ModelSerializer):
    class Meta:
        model = users_games
        fields = '__all__'