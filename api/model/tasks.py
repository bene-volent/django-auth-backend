from django.db import models
from .base import TimeStampedModel


class Task(TimeStampedModel):
    task = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    type = models.IntegerField(default=0)
    user = models.ForeignKey('User',on_delete=models.CASCADE,related_name='tasks')