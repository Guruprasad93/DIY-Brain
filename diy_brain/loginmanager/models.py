from django.db import models


# Create your models here.
class SessionData(models.Model):
    email_address = models.EmailField()
    ip_address = models.TextField()
