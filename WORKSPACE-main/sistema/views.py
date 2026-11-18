from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def medico_view(request):
    print('Página médico funcionou')
    return HttpResponse ('Página inicial do Médico')

def home(request):
    print ('Página home funcionou')
    return HttpResponse ('Página Home')

from django.contrib import admin
from django.urls import path

from sistema.views import medico_view

urlpatterns = [
    path('médico/', medico_view) # vollmed.com/medico
]