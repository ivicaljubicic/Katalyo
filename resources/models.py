from django.db import models

# Create your models here.

class Organisations(models.Model):
    Name = models.CharField(max_length=200)
    Description = models.TextField()
    Country = models.CharField(max_length=3)
    Industry = models.CharField(max_length=3)
    DefaultLang = models.CharField(max_length=10)
    Purpose = models.CharField(max_length=200)
    CreatedBy = models.CharField(max_length=200)
    CreatedDateTime = models.DateTimeField(auto_now_add=True)
    ChangedBy = models.CharField(max_length=200)
    ChangedDateTime = models.DateTimeField(auto_now=True)
    Status = models.CharField(max_length=20)
    Version = models.IntegerField()

class Addresses(models.Model):
    Organisation = models.ForeignKey(Organisations)
    StreetName = models.CharField(max_length=200)
    Number = models.CharField(max_length=20)
    Zip = models.IntegerField()
    Country = models.CharField(max_length=3)
    CreatedBy = models.CharField(max_length=200)
    CreatedDateTime = models.DateTimeField(auto_now_add=True)
    ChangedBy = models.CharField(max_length=200)
    ChangedDateTime = models.DateTimeField(auto_now=True)
    Status = models.CharField(max_length=20)
    Version = models.IntegerField()

class ResourceDef(models.Model):
    Organisation = models.ForeignKey(Organisations)
    CreatedBy = models.CharField(max_length=200)
    CreatedDateTime = models.DateTimeField(auto_now_add=True)
    ChangedBy = models.CharField(max_length=200)
    ChangedDateTime = models.DateTimeField(auto_now=True)
    Status = models.CharField(max_length=20)
    Version =models.IntegerField()
    Private=models.BooleanField()
    ResourceType=models.CharField(max_length=1)
    DefaultLang = models.CharField(max_length=10)
    
    
class ResourceDefLang(models.Model):
    Resource = models.ForeignKey(ResourceDef)
    Lang = models.CharField(max_length=10)
    Name = models.CharField(max_length=200)
    Subject = models.CharField(max_length=1000)
    Description = models.TextField()
    CreatedBy = models.CharField(max_length=200)
    CreatedDateTime = models.DateTimeField(auto_now_add=True)
    ChangedBy = models.CharField(max_length=200)
    ChangedDateTime = models.DateTimeField(auto_now=True)
    Version = models.IntegerField()
    
    
class ResourceDefFields(models.Model):
    Resource = models.ForeignKey(ResourceDef)
    FieldType = models.CharField(max_length=200)
    GenericType = models.CharField(max_length=200)
    DBType = models.CharField(max_length=200)
    Status = models.CharField(max_length=200)
    SeqNo = models.IntegerField()
    CreatedBy = models.CharField(max_length=200)
    CreatedDateTime = models.DateTimeField(auto_now_add=True)
    ChangedBy = models.CharField(max_length=200)
    ChangedDateTime = models.DateTimeField(auto_now=True)
    Version = models.IntegerField()
    
class ResourceDefFieldsLang(models.Model):
    ResourceDefFields = models.ForeignKey(ResourceDefFields)
    Lang = models.CharField(max_length=10)
    Name = models.CharField(max_length=200)
    Subject = models.CharField(max_length=1000)
    Description = models.TextField()
    CreatedBy = models.CharField(max_length=200)
    CreatedDateTime = models.DateTimeField(auto_now_add=True)
    ChangedBy = models.CharField(max_length=200)
    ChangedDateTime = models.DateTimeField(auto_now=True)
    Version =models.IntegerField()