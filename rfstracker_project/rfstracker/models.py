from django.db import models
import os

# Create your models here.

class Salesdb(models.Model):

    rfsnumber = models.CharField(max_length=254,unique=True)
    oppnumber = models.CharField(max_length=254, null=True, blank=True)
    description = models.CharField(max_length=254, blank=False)
    datecreated = models.DateField(auto_now=True)
    rfsreqfile = models.FileField(upload_to='uploads/', blank=True, null=True)
    choices = (
    ('sales','Sales Queue'),
    ('solutions','Solutions Queue'),
    ('projectmgmt','ProjectMgmt Queue'),
    ('servicemgmt','ServiceMgmt Queue'),
    ('pricing','Pricing Queue'),
    ('completed','Completed'),
    )
    queue = models.CharField(max_length=50,choices=choices,default='sales', blank=False)

    def __str__(self):
        return self.rfsnumber



class Detailsdb(models.Model):
    rfsnumber = models.ForeignKey(Salesdb,on_delete=models.CASCADE)
    datecreated = models.DateField(auto_now=True)
    comments = models.CharField(max_length=2000, null=True, blank=True)
    attachement = models.FileField(upload_to='uploads/', blank=True, null=True)
    choices = (
    ('sales','Sales Queue'),
    ('solutions','Solutions Queue'),
    ('projectmgmt','ProjectMgmt Queue'),
    ('servicemgmt','ServiceMgmt Queue'),
    ('pricing','Pricing Queue'),
    ('completed','Completed'),
    )
    queue = models.CharField(max_length=50,choices=choices,default='sales',blank=False)

    def __str__(self):
        return self.rfsnumber.rfsnumber
