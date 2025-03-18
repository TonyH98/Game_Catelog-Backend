from rest_framework import serializers
from .models import Users, game_review, users_games



class GameReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = game_review
        fields = '__all__'

class UsersGamesSeralizer(serializers.ModelSerializer):
    review = GameReviewSerializer(many = True, read_only = True)
    class Meta:
        model = users_games
        fields = '__all__'

class UsersSerializer(serializers.ModelSerializer):
    games = UsersGamesSeralizer(many = True, read_only = True)
    class Meta:
        model = Users
        fields = '__all__'