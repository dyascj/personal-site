from django.db import models

# Create your models here.

class Account(models.Model):
    
    __tablename__ = "account"
    

   
    test = models.CharField(max_length=30)
    test2 = models.CharField(max_length=30)