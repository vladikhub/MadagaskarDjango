from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.urls import reverse

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from .forms import LoginUserForm


def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'],
                                password=cd['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
    else:
        form = LoginUserForm()
    return render(request, 'clients/index.html', {'form': form})