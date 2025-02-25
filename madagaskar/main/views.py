from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here.



def start_page(request):
    if request.user.is_authenticated:
        return render(request, "main/layout.html")
    else:
        return HttpResponseRedirect(reverse('users:login'))