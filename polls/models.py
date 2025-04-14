from django.db import models
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator

class Users(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=128)  # Consider using Django's built-in password hashing
    email = models.EmailField(unique=True)  # Use EmailField instead of CharField
    account_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.username


class UserGame(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="games")
    game_title = models.CharField(max_length=255)
    console = models.CharField(max_length=100)
    release_date = models.DateField()
    game_rating = models.CharField(max_length=10)
    game_developer = models.CharField(max_length=255)
    game_publisher = models.CharField(max_length=255)
    game_art = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.game_title} ({self.console}) - {self.user.username}"


class GameReview(models.Model):
    game = models.ForeignKey(UserGame, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="reviews")
    review = models.TextField()
    score = models.IntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(100)
    ])

    def __str__(self):
        return f"Review by {self.user.username} on {self.game.game_title}"
