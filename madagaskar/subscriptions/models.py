from django.core.validators import MinValueValidator
from django.db import models

from clients.models import Client


# Create your models here.
class MinuteSubscription(models.Model):
    minutes = models.IntegerField(validators=[MinValueValidator(0)], null=True)


class UnlimitedSubscription(models.Model):
    MONTH = "М"
    HALF_YEAR = "ПГ"
    YEAR = "Г"

    MY_CHOICES = {
        MONTH: "Месяц",
        HALF_YEAR: "Полгода",
        YEAR: "Год"
    }

    period = models.CharField(choices=MY_CHOICES)
    end_at = models.DateField(null=True)


class Subscription(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE, default=None)
    number = models.IntegerField(null=False, unique=True)
    type_sub = models.CharField(null=True)
    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)
    is_active = models.BooleanField(default=True)
    minute_subscription = models.OneToOneField(MinuteSubscription, models.CASCADE, null=True, blank=True)
    unlimited_subscription = models.OneToOneField(UnlimitedSubscription, models.CASCADE, null=True, blank=True)
