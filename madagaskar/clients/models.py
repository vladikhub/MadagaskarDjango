from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField


class Subscription(models.Model):
    number = models.IntegerField(null=False, unique=True)
    minutes = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return str(self.number)


class Client(models.Model):
    name = models.CharField(max_length=17)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    subscription = models.OneToOneField(Subscription, on_delete=models.SET_NULL, null=True)

    def get_absolute_url(self):
        return reverse('main:client-info', kwargs={"client_id": self.pk})



# Create your models here.
