from dateutil.relativedelta import relativedelta
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from clients.models import Client
from main.forms import CreateClientForm, UpdateClientForm
from subscriptions.models import Subscription, MinuteSubscription, UnlimitedSubscription


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

            if phone in [client.phone for client in clients]:
                info['error'] = "Пользователь с таким номером телефона уже существует"
                return render(request, "clients/add_client.html", info)

            # if number_min:
            #     sub_num = max([subscription.number for subscription in subscriptions]) + 1
            #     minute_sub = MinuteSubscription.objects.create(minutes=number_min)
            #     Subscription.objects.create(number=sub_num, type_sub="Минутный", minute_subscription=minute_sub)
            #     subscription = Subscription.objects.get(number=sub_num)

            Client.objects.create(name=name, phone=phone)
            client = Client.objects.get(phone=phone)
            return redirect('clients:client-info', client_id=client.id)
        else:
            print(form.errors)
    else:
        form =CreateClientForm()
        info['form'] = form
        return render(request, "clients/add_client.html", info)

@login_required
def client_info(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    context = {"client": client, "subscription": client.subscription_or_none}
    return render(request, "clients/client_info.html", context)

@login_required
def update_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    info = {}
    if request.method == "POST":
        form = UpdateClientForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            phone = form.cleaned_data["phone"]
            number_min = form.cleaned_data["number_min"]
            time_period = form.cleaned_data["time_period"]
            rus_time_period = dict(UnlimitedSubscription.MY_CHOICES).get(time_period, 'Нет')
            info["form"] = form

            if name != client.name:
                client.name = name

            if phone != client.phone:
                clients = Client.objects.all()
                if phone in [client.phone for client in clients]:
                    info['error'] = "Пользователь с таким номером телефона уже существует"
                    return render(request, "clients/update_client.html", info)

                client.phone = phone


            if not client.subscription_or_none and number_min:
                subscriptions = Subscription.objects.all()
                sub_num = max([subscription.number for subscription in subscriptions] + [0]) + 1
                minute_sub = MinuteSubscription.objects.create(minutes=number_min)
                Subscription.objects.create(number=sub_num, type_sub="Минутный", minute_subscription=minute_sub, client=client)
                subscription = Subscription.objects.get(number=sub_num)
                client.subscription = subscription

            elif client.subscription_or_none and client.subscription.type_sub == "Минутный" and number_min != client.subscription.minute_subscription.minutes:
                client.subscription.minute_subscription.minutes = number_min

            elif not client.subscription_or_none and time_period != "":
                subscriptions = Subscription.objects.all()
                sub_num = max([subscription.number for subscription in subscriptions] + [0]) + 1

                unlim_sub = UnlimitedSubscription.objects.create(period=time_period)
                Subscription.objects.create(number=sub_num, type_sub="Безлимитный", unlimited_subscription=unlim_sub, client=client)
                subscription = Subscription.objects.get(number=sub_num)
                months=0
                if time_period == "Месяц":
                    months = 1
                elif time_period == "Полгода":
                    months = 6
                else:
                    months = 12
                data_end = subscription.created_at + relativedelta(months=+months)
                client.subscription = subscription
                unlim_sub.end_at = data_end
                unlim_sub.save()
            elif client.subscription_or_none and client.subscription.type_sub == "Безлимитный" and time_period != client.subscription.unlimited_subscription.period:
                client.subscription.unlimited_subscription.period = time_period


            client.save()
            client.subscription.save()

            return redirect('clients:client-info', client_id=client.id)
    else:
        form = UpdateClientForm()
        info['form'] = form
        info['client'] = client
        info['phone'] = str(client.phone)[2:]
        return render(request, "clients/update_client.html", info)

@login_required
def delete_client(request, client_id: int):
    if request.method == "POST":
        user = get_object_or_404(Client, id=client_id)
        user.delete()
        return redirect('main:home')

# Create your views here.

'''
Сделать разделение на того, кто вошел
'''