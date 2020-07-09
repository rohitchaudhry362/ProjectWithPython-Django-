from django.db import models

class Hello2(models.Model):
    CatId=models.AutoField(primary_key=True)
    CatName=models.CharField(max_length=100)
