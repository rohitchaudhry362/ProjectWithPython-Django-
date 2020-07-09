from django.db import models
from django.contrib.auth.models import User

class Hello(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
