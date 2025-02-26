from django import forms
from phonenumber_field.formfields import PhoneNumberField

class CreateClientForm(forms.Form):
    name = forms.CharField(label="Имя",
                           widget=forms.TextInput(attrs={'class': 'form-input'}))
    phone = PhoneNumberField(label="Номер телефона")
