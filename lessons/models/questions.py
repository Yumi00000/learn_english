from django.db import models
from .lessons import Lessons

class Questions(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.TextField()
    wrong_answer = models.TextField()
    correct_answer = models.TextField()
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE)

    def __str__(self):
        return self.id