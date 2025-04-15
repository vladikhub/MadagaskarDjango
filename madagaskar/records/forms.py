from email.policy import default

from django import forms

from clients.models import Client
from creams.models import Creams
from records.models import ClientRecords


class ClientRecordsForm(forms.Form):
    by_subscription = forms.ChoiceField(
        choices=[(True, "Да"), (False, "Нет")],
        label="По абонементу",
        widget=forms.Select
    )
    cream = forms.ModelChoiceField(queryset=Creams.objects.all(), initial=None, required=False, label="Крем")
    weight = forms.FloatField(required=False, label="Вес", initial=None)
    discount = forms.IntegerField(required=False, label="Скидка", initial=None)
    tanning_booth = forms.ChoiceField(choices=ClientRecords.MY_CHOICES_CAB, label="Кабинка")
    minutes = forms.IntegerField(label="Минуты")