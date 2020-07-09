from django.db import models
from django.utils import timezone

class BookCategory1(models.Model):
    BookCatId=models.AutoField(primary_key=True)
    BookCatName=models.CharField(max_length=100)
    BookCategoryImg=models.ImageField(upload_to="Library_media",blank=True,null=True)

    def __str__(self):
        return self.BookCatName

class Stream1(models.Model):
    BookCatId=models.ForeignKey(BookCategory1,on_delete=models.CASCADE)
    StreamId=models.AutoField(primary_key=True)
    StreamName=models.CharField(max_length=100)
    class Meta:
        get_latest_by='StreamId'


class Book1(models.Model):
    BookCatId=models.ForeignKey(BookCategory1,on_delete=models.CASCADE)
    StreamId=models.ForeignKey(Stream1,on_delete=models.CASCADE)
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

class BookStock1(models.Model):
    BookStockId=models.AutoField(primary_key=True)
    BookId=models.ForeignKey(Book1,on_delete=models.CASCADE)
    BookStockSerial=models.CharField(max_length=100)
    Issued=models.BooleanField(default=False)

class BookCart1(models.Model):
    #TempId=models.AutoField(primary_key=True)
    BookId=models.IntegerField(blank=True,null=True)
    BookName=models.CharField(max_length=100,default="MYBOOK")
    BookAuthorName=models.CharField(max_length=100,blank=True,default=True)
    BookSerialNumber=models.CharField(max_length=100,null=True,blank=True)
    BookStockSerial=models.CharField(max_length=100,default=1)
    Edition=models.IntegerField(blank=True,null=True)

class LibraryOrder1(models.Model):
    LibOrderId=models.AutoField(primary_key=True)
    UserId=models.IntegerField(default=True)
    DateOfOrder=models.DateField(auto_now_add=True)
    class Meta:
        get_latest_by='LibOrderId'

class LibOrderDetails1(models.Model):
    LODId=models.AutoField(primary_key=True)
    LibOrderId=models.ForeignKey(LibraryOrder1,on_delete=models.CASCADE)
    BookId=models.IntegerField(default=True)
    BookName=models.CharField(max_length=100,default="MYBOOK")
    BookSerialNumber=models.CharField(max_length=100,null=True,blank=True)
    BookStockSerial=models.CharField(max_length=100,default="01")
    IsReturned=models.BooleanField(default=False)

class ReturnBook(models.Model):
    ReturnId=models.AutoField(primary_key=True)
    BookStockSerial=models.CharField(max_length=100,default="01")
    DateOfOrder=models.DateField(blank=True)
    ReturnDate=models.DateField(auto_now_add=True)
    #Fine=models.IntegerField(null=True)

    class Meta:
        get_latest_by='ReturnId'

class FineAmount1(models.Model):
    FaId=models.AutoField(primary_key=True)
    User=models.IntegerField(default=True)
    DateOfFine=models.DateField(auto_now_add=True)
    FineAmount=models.IntegerField(default=0)
