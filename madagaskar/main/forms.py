from django import forms
from phonenumber_field.formfields import SplitPhoneNumberField


class DemoSplitPhoneNumberField(SplitPhoneNumberField):
    def prefix_field(self):
        return forms.ChoiceField(choices=[
            ("RU", "+7"),
        ], widget=forms.Select(attrs={'style': "width: 50px; height: 40px; border-radius: 20%;"}))
    def number_field(self):
        return forms.CharField(
        widget=forms.TextInput(attrs={'style': "width: 180px; height: 40px; border-radius: 10%;"}))


class CreateClientForm(forms.Form):
    name = forms.CharField(label="Имя",
                           widget=forms.TextInput(attrs={'class': 'form-input'}))
    phone = DemoSplitPhoneNumberField(label="Номер телефона", region="RU")
    number_min = forms.IntegerField(label="Количество минут",
                                    required=False,
                                    help_text="Введите количество минут, если клиент приобретает абонемент")

