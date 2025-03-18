from django.db import models
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Users(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable=False)
    username = models.CharField(max_length = 30)
    firstname = models.CharField(max_length = 30)
    lastname = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)
    email = models.CharField(max_length = 50)
    account_date = models.DateField()


class users_games(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    game_title = models.CharField()
    console = models.CharField()
    release_date = models.DateField()
    game_rating = models.CharField()
    game_console = ArrayField(models.CharField(), blank=True, default=list)
    game_dev = models.CharField()
    game_publisher = models.CharField()
    game_art = models.CharField()



class game_review(models.Model):
    game_title = models.ForeignKey(users_games, on_delete=models.CASCADE)
    users_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    review = models.TextField()
    score = models.IntegerField(validators= [
        MinValueValidator(0),
        MaxValueValidator(100)
    ])