from django.db import models
import uuid


class User(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)


# Create your models here.
class TodoItem(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    title = models.CharField(max_length=200)
    completed = models.BooleanField()
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
