from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import empresa

class empresaCreate(CreateView):
    model = empresa
    fields = ['nome']

