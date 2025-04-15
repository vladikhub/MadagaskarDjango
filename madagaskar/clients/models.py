from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField

from creams.models import Creams



class Client(models.Model):
    name = models.CharField(max_length=18)
    phone = PhoneNumberField(null=False, blank=False, unique=True)

    def get_absolute_url(self):
        return reverse('clients:client-info', kwargs={"client_id": self.pk})

    @property
    def subscription_or_none(self):
        return getattr(self, 'subscription', None)






# Create your models here.
