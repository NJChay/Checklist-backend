from django.db import models
import uuid


class User(models.Model):
    name = models.CharField(max_length=200)


# Create your models here.
class TodoItem(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    title = models.CharField(max_length=200)
    completed = models.BooleanField()
    #user = models.ForeignKey(User, on_delete=models.CASCADE)


