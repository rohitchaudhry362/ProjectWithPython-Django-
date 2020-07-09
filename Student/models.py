from django.db import models
from users.models import Student

class Documents(models.Model):
    enroll=models.IntegerField(primary_key=True,unique=True,blank=False,default=151260107099)
    adharcard=models.FileField(upload_to="documents",blank=True,null=True)
    result10=models.FileField(upload_to="documents",blank=True,null=True)
    result12=models.FileField(upload_to="documents",blank=True,null=True)
    semresult1=models.FileField(upload_to="documents",blank=True,null=True)
    semresult2=models.FileField(upload_to="documents",blank=True,null=True)
    semresult3=models.FileField(upload_to="documents",blank=True,null=True)
    semresult4=models.FileField(upload_to="documents",blank=True,null=True)
    semresult5=models.FileField(upload_to="documents",blank=True,null=True)
    semresult6=models.FileField(upload_to="documents",blank=True,null=True)
    semresult7=models.FileField(upload_to="documents",blank=True,null=True)
