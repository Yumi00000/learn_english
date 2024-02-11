from django.contrib.auth.models import User
from django.db import models


class UserDictionary(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    word = models.CharField(max_length=100)
    translation = models.CharField(max_length=100)
    transcription = models.CharField(max_length=100)
    transliteration = models.CharField(max_length=100)
    audio = models.CharField(max_length=100)
