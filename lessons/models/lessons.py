from django.db import models


class Lessons(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    body = models.TextField()

    def __str__(self):
        return self.id
