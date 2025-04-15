from django.db import models

from clients.models import Client
from creams.models import Creams


# Create your models here.
class ClientRecords(models.Model):
    VERTICAL = "В"
    HORIZONTAL = "Г"
    YES = "Д"
    NO = "Н"

    MY_CHOICES_CAB = [
        (VERTICAL, "Вертикальный"),
        (HORIZONTAL, "Горизонтальный")
    ]

    MY_CHOICES_SUB = [
        (YES, "Да"),
        (NO, "Нет")
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    by_subscription = models.BooleanField()
    cream = models.ForeignKey(Creams, on_delete=models.CASCADE, null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    discount = models.IntegerField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    tanning_booth = models.CharField(max_length=2, choices=MY_CHOICES_CAB)
    minutes = models.IntegerField()