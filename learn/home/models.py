from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
#makemigration create chnages and store in a file migrate means apply the changes created by make migration
class Contact(models.Model):

    name=models.CharField(max_length=122,null=True)
    email=models.CharField(max_length=122,null=True)
    phone=models.CharField(max_length=12,null=True)
    desc=models.TextField(null=True,blank=True)
    date=models.DateTimeField(auto_now_add=True)



def __str__(self):
    return self.name



