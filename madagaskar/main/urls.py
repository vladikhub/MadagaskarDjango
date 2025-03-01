
from django.urls import path
from . import views


app_name="main"

urlpatterns = [
    path('add-client/', views.add_client, name='add-client'),
    path('client_info/<int:client_id>', views.client_info, name='client-info'),
    path('update_client/<int:client_id>', views.update_client, name='update-client')
]