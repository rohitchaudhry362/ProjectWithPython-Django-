from django.db import models
from django.utils import timezone

class BookCategory(models.Model):
    BookCatId=models.AutoField(primary_key=True)
    BookCatName=models.CharField(max_length=100)
    BookCategoryImg=models.ImageField(upload_to="Library_media",blank=True,null=True)

    def __str__(self):
        return self.BookCatName

class Stream(models.Model):
    BookCatId=models.ForeignKey(BookCategory,on_delete=models.CASCADE)
    StreamId=models.AutoField(primary_key=True)
    StreamName=models.CharField(max_length=100)
    class Meta:
        get_latest_by='StreamId'


class Book(models.Model):
    BookCatId=models.ForeignKey(BookCategory,on_delete=models.CASCADE)
    StreamId=models.ForeignKey(Stream,on_delete=models.CASCADE)
    BookId=models.AutoField(primary_key=True)
    BookName=models.CharField(max_length=100,default="MYBOOK")
    Price=models.IntegerField(default=50)
    Edition=models.IntegerField(blank=True,null=True)
    CoverPageImg=models.ImageField(upload_to="Library_media",blank=True,null=True)
    BookSerialNumber=models.CharField(max_length=100,null=True,blank=True)
    PublishingYear=models.DateTimeField(auto_now_add=True)
    BookAuthorName=models.CharField(max_length=100,blank=True,default=True)

    class Meta:
        get_latest_by="BookId"


class BookCart(models.Model):
    #TempId=models.AutoField(primary_key=True)
    BookId=models.IntegerField(blank=True,null=True)
    BookName=models.CharField(max_length=100,default="MYBOOK")
    BookAuthorName=models.CharField(max_length=100,blank=True,default=True)
    BookSerialNumber=models.CharField(max_length=100,null=True,blank=True)
    BookStockSerial=models.CharField(max_length=100,default=1)
    Edition=models.IntegerField(blank=True,null=True)

    #Price=models.IntegerField(default=50)
    #quantity=models.IntegerField(null=False)


class BookStock(models.Model):
    BookStockId=models.AutoField(primary_key=True)
    BookId=models.ForeignKey(Book,on_delete=models.CASCADE)
    BookStockSerial=models.CharField(max_length=100)
    Issued=models.BooleanField(default=False)


class BookReturn(models.Model):
    BookReturnId=models.AutoField(primary_key=True)
    UserId=models.IntegerField(default=True)
    BookStockId=models.ForeignKey(BookStock,on_delete=models.CASCADE)
    BookId=models.IntegerField(default=0)
    DateOfReturn=models.DateTimeField(auto_now_add=True)
    Fine=models.IntegerField()

class LibraryOrder(models.Model):
    LibOrderId=models.AutoField(primary_key=True)
    UserId=models.IntegerField(default=True)
    DateOfOrder=models.DateTimeField(auto_now_add=True)
    class Meta:
        get_latest_by='LibOrderId'

class LibOrderDetails(models.Model):
    LODId=models.AutoField(primary_key=True)
    LibOrderId=models.ForeignKey(LibraryOrder,on_delete=models.CASCADE)
    BookId=models.IntegerField(default=True)
    BookSerialNumber=models.CharField(max_length=100,null=True,blank=True)
    BookStockSerial=models.CharField(max_length=100,default="01")
    Date=models.DateTimeField(default=timezone.now)
