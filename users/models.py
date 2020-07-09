from django.db import models
from django.contrib.auth.models import User


class Role(models.Model):
    Roleid=models.AutoField(primary_key=True)
    rolename=models.CharField(max_length=40)
    roleimg=models.ImageField(upload_to="users_media",blank=True,null=True)

class UserProfile(models.Model):
    id=models.AutoField(primary_key=True,default=0)
    userdata=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    DOB=models.DateField()
    Roleid=models.IntegerField(default=0)
    userimg=models.ImageField(upload_to="users_media",blank=True,null=True)
User.profile=property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

class MyUser(models.Model):
    user=models.CharField(max_length=30,unique=True)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField(null=False,blank=False)
    uniqueid=models.IntegerField()
    phone_number = models.CharField(max_length=15,default="+910000000000")
    userimg=models.ImageField(upload_to="users_media",blank=True,null=True)

class Student(models.Model):
    STREAM_CHOICES = (
    ("Computer","COM_SCIENCE"),
    ("Chemical","CHEMICAL"),
    ("Mechanical","MECHANICAL"),
    ("Civil","CIVIL"),
)

    enroll=models.IntegerField(primary_key=True)
    user=models.CharField(max_length=30,unique=True)
    sem=models.IntegerField(null=False,blank=False)
    stream=models.CharField(max_length=30,choices=STREAM_CHOICES)
    balance=models.IntegerField(default=0)

class card(models.Model):
    enroll=models.IntegerField(primary_key=True)
    isblocked=models.BooleanField(default=False)

class Query(models.Model):
    queryid=models.AutoField(primary_key=True)
    querytext=models.CharField(null=False,blank=False,max_length=500,default="this is a query")
    date=models.DateTimeField(auto_now_add=True)
    isreviewed=models.BooleanField(default=False)

class mobile(models.Model):
    mobilenumber=models.CharField(max_length=15,default="+910000000000")
    otp=models.IntegerField(default=10)

    class Meta:
        get_latest_by='mobilenumber'
