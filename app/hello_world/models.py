from django.db import models

# Create your models here.
class NewClass(models.Model):
    Id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=500)



class Student(models.Model):
    Id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    ClassId = models.ForeignKey("NewClass", on_delete=models.CASCADE)


