from django.db import models

class Donor(models.Model):
    name= models.CharField(max_length=100)
    blood_group= models.CharField(max_length=5)
    email= models.EmailField()
    phone_number= models.IntegerField()
    
