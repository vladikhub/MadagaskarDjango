from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from clients.models import Client
from .forms import CreateClientForm

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

    return render(request, "clients/client_page.html", info)

def show_staff_page(request):
    return render(request, "main/layout.html")

@login_required
def add_client(request):
    clients = Client.objects.all()
    info = {}
    if request.method == "POST":
        form = CreateClientForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            phone = form.cleaned_data["phone"]

            info["form"] = form
            print(clients)
            if phone in [client.phone for client in clients]:
                info['error'] = "Пользователь с таким номером телефона уже существует"
                return render(request, "main/add_client.html", info)

            Client.objects.create(name=name, phone=phone, subscription=None)
            return HttpResponseRedirect(reverse('home'))
    else:
        form =CreateClientForm()
        info['form'] = form
        return render(request, "main/add_client.html", info)

@login_required
def update_client(request):
    pass

