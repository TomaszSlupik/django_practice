from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Tworzymy endpointy - logika biznesowa 
def hi(request):
    return HttpResponse ('<h1> Ćwiczymy </h1>')