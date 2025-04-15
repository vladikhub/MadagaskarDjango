from django.urls import path
from clients.views import add_client, client_info, update_client, delete_client
from records.views import create_record
app_name="clients"

urlpatterns = [
    path('add-client/', add_client, name='add-client'),
    path('client_info/<int:client_id>', client_info, name='client-info'),
    path('update_client/<int:client_id>', update_client, name='update-client'),
    path('delete_client/<int:client_id>', delete_client, name='delete-client'),
    path('create_record/<int:client_id>', create_record, name="create-record")
]