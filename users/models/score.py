from django.db import models

from .user import User


class Score(models.Model):
    id = models.ForeignKey(User.id, on_delete=models.CASCADE)
    value = models.IntegerField()

    def __str__(self):
        return self.id