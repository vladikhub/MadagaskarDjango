from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Client(models.Model):
    name = models.CharField(max_length=16)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    subscription = models.IntegerField(null=True, blank=True)



# Create your models here.
