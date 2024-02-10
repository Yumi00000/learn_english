from django.db import models

from lessons.models import Lessons


class User(models.Model):
    id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.TextField()
    name = models.TextField()
    surname = models.TextField()

    def __str__(self):
        return str(self.id)


class UserProgress(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lessons = models.ForeignKey(Lessons, on_delete=models.CASCADE)
    score = models.IntegerField()
