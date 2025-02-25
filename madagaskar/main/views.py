from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from users.models import Client

# Create your views here.



def start_page(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return render(request, "main/layout.html")
        else:
            return HttpResponseRedirect(reverse('client'))
    else:
        return HttpResponseRedirect(reverse('users:login'))

def show_client_page(request):
    client = Client.objects.get(user=request.user)
    info = {
        'first_name': client.name,
        'phone': client.phone,
        'subscription': client.subscription
            }

    return render(request, "users/client_page.html", info)