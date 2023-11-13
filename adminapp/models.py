from django.db import models

# Create your models here.

class course(models.Model):
    courseid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=25)
    duration=models.IntegerField()
    fees=models.IntegerField()
    details=models.CharField(max_length=200)

class batch(models.Model):
    courseid= models.ForeignKey(course,on_delete=models.CASCADE)
    batchid=models.AutoField(primary_key=True)
    startdate=models.DateField()
    batchtime=models.CharField(max_length=30)
    facultyname=models.CharField(max_length=40)
    batchstatus=models.IntegerField()

class course1(models.Model):
    courseid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=25)
    duration=models.IntegerField()
    fees=models.IntegerField()
    details=models.CharField(max_length=200)
    courseicon=models.CharField(max_length=60)