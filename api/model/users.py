from django.db import models

from .base import TimeStampedModel


class User(TimeStampedModel):
    """Model definition for User."""
    fname = models.CharField(max_length=30)
    lname = models.CharField(db_default=None,max_length=30)
    username = models.CharField(unique=True,db_index=True,max_length=256)
    email = models.EmailField()
    hashed_password = models.CharField(max_length=72)
    
    class Meta:
        """Meta definition for User."""

        verbose_name = 'User'
        verbose_name_plural = 'Users'

   
