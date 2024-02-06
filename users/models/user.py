from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.TextField()
    name = models.TextField()
    surname = models.TextField()

    def __str__(self):
        return self.id
