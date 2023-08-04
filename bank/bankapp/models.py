from django.db import models
from datetime import date

# Create your models here.
class Employee(models.Model):
    eid = models.IntegerField( default='')
    ename = models.CharField(max_length=100, default='')
    email = models.EmailField(default='')
    dob = models.DateField(default='')
    econtact = models.BigIntegerField( default='')
    econtact2 = models.BigIntegerField(default='')
    qualification = models.CharField(max_length=50, default='')
    doj = models.DateField(default='')
    aadhar = models.CharField(max_length=100)
    pan = models.CharField(max_length=100, default='')
    address = models.TextField(max_length=100, default='')
    blood = models.CharField(max_length=50, default='')
    def __str__(self):
        return "%s" %self.ename




class Bank(models.Model):
    eid = models.IntegerField(default='')
    name = models.CharField(max_length=100, default='')
    accno = models.BigIntegerField(default='')
    ifsc = models.CharField(max_length=100, default='')
    branch_name = models.CharField(max_length=100)
    city = models.CharField(max_length=50, default='')
    state = models.CharField(max_length=50, default='')

    def __str__(self):
        return "%s" %self.name

    
    

