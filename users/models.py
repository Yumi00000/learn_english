from django.contrib.auth.models import User
from django.db import models

from lessons.models import Lessons





class UserProgress(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lessons = models.ForeignKey(Lessons, on_delete=models.CASCADE)
    score = models.IntegerField()
