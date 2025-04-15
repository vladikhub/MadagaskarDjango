from django.shortcuts import render, redirect, get_object_or_404

from clients.models import Client
from records.models import ClientRecords
from records.forms import ClientRecordsForm


# Create your views here.

def create_record(request, client_id: int):
    if request.method == "POST":
        print(1)
        form = ClientRecordsForm(request.POST)
        if form.is_valid():
            client = get_object_or_404(Client, id=client_id)
            by_subscription = form.cleaned_data["by_subscription"]
            cream = form.cleaned_data["cream"]
            weight = form.cleaned_data["weight"]
            discount = form.cleaned_data["discount"]
            tanning_booth = form.cleaned_data["tanning_booth"]
            minutes = form.cleaned_data["minutes"]
            ClientRecords.objects.create(
                client=client,
                by_subscription=by_subscription,
                cream = cream,
                weight = weight,
                discount = discount,
                tanning_booth = tanning_booth,
                minutes = minutes
            )
            print(1)
            return redirect('main:home')
        else:
            print(form.errors)
    else:
        form = ClientRecordsForm()
    return render(request, 'records/add_record.html', {'form': form})