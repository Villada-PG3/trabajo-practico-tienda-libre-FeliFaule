from django.shortcuts import render
from django.views.generic import TemplateView


def home(request):
    return render(request, "tiendalibre/home.html")


def acerca_de_mi(request):
    return render(request, "tiendalibre/acerca_de_mi.html")
