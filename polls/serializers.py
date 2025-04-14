from rest_framework import serializers
from .models import Users, GameReview, UserGame

class GameReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameReview
        fields = '__all__'

class UserGameSerializer(serializers.ModelSerializer):
    reviews = GameReviewSerializer(many=True, read_only=True)  # Use 'reviews' to match related_name in GameReview

    class Meta:
        model = UserGame
        fields = '__all__'

class UsersSerializer(serializers.ModelSerializer):
    games = UserGameSerializer(many=True, read_only=True)  # Use 'games' to match related_name in UserGame

    class Meta:
        model = Users
        fields = '__all__'
