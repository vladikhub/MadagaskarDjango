from django.contrib import admin
from .models import Client, Subscription
# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'subscription')

@admin.register(Subscription)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('number', 'minutes')