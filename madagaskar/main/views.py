from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from clients.models import Client
from .forms import CreateClientForm

"Номер абонемента добавляется макс + 1"

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
    sub_num = None
    if request.method == "POST":
        form = CreateClientForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            phone = form.cleaned_data["phone"]
            number_min = form.cleaned_data["number_min"]

            info["form"] = form

            if phone in [client.phone for client in clients]:
                info['error'] = "Пользователь с таким номером телефона уже существует"
                return render(request, "main/add_client.html", info)

            if number_min:
                sub_num = max([client.subscription for client in clients]) + 1

            Client.objects.create(name=name, phone=phone, subscription=sub_num)
            client = Client.objects.get(phone=phone)
            return redirect('main:client-info', client_id=client.id)
        else:
            print(form.errors)
    else:
        form =CreateClientForm()
        info['form'] = form
        return render(request, "main/add_client.html", info)

@login_required
def client_info(request, client_id):
    client = Client.objects.get(id=client_id)
    return render(request, "main/client_info.html")

