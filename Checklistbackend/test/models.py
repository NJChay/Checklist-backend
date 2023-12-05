from django.db import models


# Create your models here.
class TodoItem(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    title = models.CharField(max_length=200)
    completed = models.BooleanField()
