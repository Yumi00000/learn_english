from django.db import models


class Lessons(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    body = models.TextField()


class Questions(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.TextField()
    wrong_answer = models.TextField()
    correct_answer = models.TextField()
    lesson_id = models.ForeignKey(Lessons, on_delete=models.CASCADE)
