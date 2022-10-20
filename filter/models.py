from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    position=models.CharField(max_length=100)
    Age=models.PositiveIntegerField()
    def __str__(self):
        return '%s%s%s%s' %(self.first_name,self.last_name,self.position,self.Age)