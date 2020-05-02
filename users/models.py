from django.db import models
from django.contrib.auth.models import User

class Points(models.Model):
    username = models.CharField(max_length=150)
    points = models.IntegerField(default=0)
# Create your models here.

    def __str__(self):
        return self.username
