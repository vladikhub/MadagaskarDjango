from django.contrib import admin

from records.models import ClientRecords


# Register your models here.
@admin.register(ClientRecords)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'by_subscription',
                    'cream', 'weight', 'discount', 'date',
                    'time', 'tanning_booth', 'minutes')