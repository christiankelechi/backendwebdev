from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ClassList(models.Model):
    first_name=models.CharField(max_length=2000)
    last_name=models.CharField(max_length=4000)
    phone_number=models.CharField(max_length=4000,null=True,blank=True)
