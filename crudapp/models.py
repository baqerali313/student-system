from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50, null=True)
    class_st = models.CharField(max_length=50, null=True)
    age = models.IntegerField(null=True)
    city = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name
