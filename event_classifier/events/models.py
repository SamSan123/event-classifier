from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    description = models.TextField()
    date = models.DateTimeField()
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

def __str__(self):
    return self.name

def snippet(self):
    return self.description[:50] + "..."