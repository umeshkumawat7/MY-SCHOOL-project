from django.db import models

class mstuser(models.Model):
    sno=models.AutoField(primary_key=True)
    fnm=models.CharField(max_length=25)
    dob=models.DateField()
    gender=models.CharField(max_length=15)
    address=models.CharField(max_length=70)
    city=models.CharField(max_length=15)
    emailid=models.CharField(max_length=50)
    pwd=models.CharField(max_length=15)
    role=models.CharField(max_length=15)

class register1(models.Model):
    sno=models.AutoField(primary_key=True)
    fnm=models.CharField(max_length=25)
    dob=models.DateField()
    gender=models.CharField(max_length=15)
    address=models.CharField(max_length=70)
    city=models.CharField(max_length=15)
    emailid=models.CharField(max_length=50)
    pwd=models.CharField(max_length=15)
    role=models.CharField(max_length=15)    