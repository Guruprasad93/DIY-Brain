from django.db import models


# Create your models here.
class UserData(models.Model):
    full_name = models.TextField()
    email_address = models.EmailField()
    password = models.TextField()
