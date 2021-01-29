from django.db import models


# Create your models here.
class UserBrainMap(models.Model):
    userID = models.IntegerField()
    taskName = models.CharField(max_length=200)
    taskDescription = models.CharField(max_length=1000)
