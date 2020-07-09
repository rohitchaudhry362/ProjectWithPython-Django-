from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Ccategory(models.Model):
    CatId=models.AutoField(primary_key=True)
    CatName=models.CharField(max_length=100)
    CatImg=models.ImageField(upload_to="Ccategory_media",blank=True,null=True)
    def __str__(self):
        return self.CatName



class Cproduct(models.Model):
    CatId=models.ForeignKey(Ccategory,on_delete=models.CASCADE)
    Pid=models.AutoField(primary_key=True)
    PName=models.CharField(max_length=100)
    Price=models.IntegerField()
    PImg=models.ImageField(upload_to="Cproduct_media",blank=True,null=True)
    IsAvailable=models.BooleanField(default=True)
    def __str__(self):
        return self.PName
    class Meta:
        get_latest_by='Pid'


class CartProduct(models.Model):

    #TempId=models.AutoField(primary_key=True)
    Pid=models.ForeignKey(Cproduct,on_delete=models.CASCADE)
    Price=models.IntegerField(default=50)
    quantity = models.IntegerField(default=1)
    class Meta:
        get_latest_by='Pid'

class CatOrder(models.Model):
    CatOrderId=models.AutoField(primary_key=True)
    UserId=models.IntegerField(default=True)
    DateOfOrder=models.DateTimeField(auto_now_add=True)
    class Meta:
        get_latest_by='CatOrderId'


class CatOrderDetails(models.Model):
    CODId=models.AutoField(primary_key=True)
    CatOrderId=models.ForeignKey(CatOrder,on_delete=models.CASCADE)
    Pid=models.ForeignKey(Cproduct,on_delete=models.CASCADE)
    Price=models.IntegerField(default=True)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])

class Mydetails(models.Model):
    Id=models.AutoField(primary_key=True)
    CatName=models.CharField(max_length=100)
