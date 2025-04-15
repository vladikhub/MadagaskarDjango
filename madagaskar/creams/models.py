from django.db import models



# Create your models here.
class Creams(models.Model):
    title = models.CharField(unique=True, null=False)
    cost = models.FloatField()

