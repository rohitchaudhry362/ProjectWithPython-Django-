from django.db import models

class BookCategory(models.Model):
    BcId=models.AutoField(primary_key=True)
    BcName=models.CharField(max_length=100)
    def __str__(self):
        return self.BcName

class Stream(models.Model):
    StreamId=models.AutoField(primary_key=True)
    StreamName=models.CharField(max_length=100)
    def __str__(self):
        return self.StreamName
class Book(models.Model):
    BookId=models.AutoField(primary_key=True)
    BookName=models.CharField(max_length=100)
    BcId=models.ForeignKey(BookCategory,on_delete=models.CASCADE)
    StreamId=models.ForeignKey(Stream,on_delete=models.CASCADE)
    Price=models.IntegerField()
    edition=models.IntegerField()
    CoverPageImg=models.ImageField(upload_to="Stream_media",blank=True,null=True)
    BackPageImg=models.ImageField(upload_to="Stream_media",blank=True,null=True)
    def __str__(self):
        return self.BookName
class BookAuthor(models.Model):
    BookId=models.ForeignKey(Book,on_delete=models.CASCADE)
    BaID=models.AutoField(primary_key=True)
    AuthorName=models.CharField(max_length=200)
