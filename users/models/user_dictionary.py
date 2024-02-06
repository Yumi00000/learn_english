from .user import User
from django.db import models

class UserDictionary(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User.id, on_delete=models.CASCADE)
    word = models.TextField()
    translation = models.TextField()
    transcription = models.TextField()
    transliteration = models.TextField()
    audio = models.TextField()
