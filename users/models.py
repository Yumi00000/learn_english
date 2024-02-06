from django.db import models

from lessons.__init__ import Lessons


class User(models.Model):
    id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.TextField()
    name = models.TextField()
    surname = models.TextField()

class Score(models.Model):
    id = models.ForeignKey('User', on_delete=models.CASCADE)
    value = models.IntegerField()

class UserProgress(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    lessons_id = models.ForeignKey(Lessons, on_delete=models.CASCADE)
    score = models.IntegerField()

class UserDictionary(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    word = models.TextField()
    translation = models.TextField()
    transcription = models.TextField()
    transliteration = models.TextField()
    audio = models.TextField()