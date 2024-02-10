from django.db import models

from users.models import User


class UserDictionary(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    word = models.TextField()
    translation = models.TextField()
    transcription = models.TextField()
    transliteration = models.TextField()
    audio = models.TextField()
