from django.db import models
import uuid
# Create your models here.

class Users(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable=False)
    username = models.CharField(max_length = 30)
    firstname = models.CharField(max_length = 30)
    lastname = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)
    email = models.CharField(max_length = 50)
    account_date = models.DateField()

class game_review(models.Model):
    title = models.CharField(max_length = 30)
    score = models.CharField()

