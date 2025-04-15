from django.contrib import admin
from .models import Client
from subscriptions.models import MinuteSubscription, UnlimitedSubscription, Subscription
# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone')

@admin.register(Subscription)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'number', 'type_sub', 'created_at', 'updated_at', 'is_active', 'minute_subscription', 'unlimited_subscription')


@admin.register(MinuteSubscription)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'minutes')


@admin.register(UnlimitedSubscription)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'period', 'end_at')


