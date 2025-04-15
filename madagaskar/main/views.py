from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from dateutil.relativedelta import relativedelta

from clients.models import Client
from subscriptions.models import Subscription, MinuteSubscription, UnlimitedSubscription
from .forms import CreateClientForm, UpdateClientForm


# Create your views here.

def start_page(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return HttpResponseRedirect(reverse('main:home'))
        else:
            return HttpResponseRedirect(reverse('clients'))
    else:
        return HttpResponseRedirect(reverse('users:login'))


def show_staff_page(request):
    return render(request, "main/home.html")


@login_required
def home_page(request):
    data = {}
    query = request.GET.get("query", "")
    if query:
        data["clients"] = Client.objects.all().filter(phone__endswith=query)
    else:
        data["clients"] = Client.objects.all()
    return render(request, "clients/home.html", data)



def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


