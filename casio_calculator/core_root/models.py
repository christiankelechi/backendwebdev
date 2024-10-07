from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
  first_name=models.CharField(max_length=1000,blank=True)
  last_name=models.CharField(max_length=1000,blank=True)
  email=models.EmailField(max_length=200,blank=True)
  phone_number=models.TextField()
# class Register(User):
#     class Meta:
#         fields=['username','first_name','last_name','password']
        