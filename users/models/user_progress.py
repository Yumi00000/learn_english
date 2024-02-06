from lessons.models.lessons import Lessons
from .user import User
from django.db import models

class UserProgress(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User.id, on_delete=models.CASCADE)
    lessons_id = models.ForeignKey(Lessons.id, on_delete=models.CASCADE)
    score = models.IntegerField()