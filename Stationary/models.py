from django.db import models

class Scategory(models.Model):
    CatId=models.AutoField(primary_key=True)
    CatName=models.CharField(max_length=100)
    CatImg=models.ImageField(upload_to="Scategory_media",blank=True,null=True)
    def __str__(self):
        return self.CatName



class Sproduct(models.Model):
    CatId=models.ForeignKey(Scategory,on_delete=models.CASCADE)
    Pid=models.AutoField(primary_key=True)
    PName=models.CharField(max_length=100)
    Price=models.IntegerField()
    PImg=models.ImageField(upload_to="Sproduct_media",blank=True,null=True)
    IsAvailable=models.BooleanField(default=True)
    def __str__(self):
        return self.PName
    class Meta:
        get_latest_by='Pid'

class CartProduct(models.Model):
    #TempId=models.AutoField(primary_key=True)
    Pid=models.ForeignKey(Sproduct,on_delete=models.CASCADE)
    Price=models.IntegerField(default=50)
    quantity=models.IntegerField(null=False)
    class Meta:
        get_latest_by='Pid'


class StatOrder(models.Model):
    StatOrderId=models.AutoField(primary_key=True)
    UserId=models.IntegerField(default=True)
    DateOfOrder=models.DateTimeField(auto_now_add=True)
    class Meta:
        get_latest_by='StatOrderId'

class StatOrderDetails(models.Model):
    SODId=models.AutoField(primary_key=True)
    StatOrderId=models.ForeignKey(StatOrder,on_delete=models.CASCADE)
    Pid=models.ForeignKey(Sproduct,on_delete=models.CASCADE)
    Price=models.IntegerField(default=True)
    quantity=models.IntegerField(null=False)
