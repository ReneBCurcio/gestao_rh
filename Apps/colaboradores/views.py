from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Colaboradores


class Colaboradoreslist(ListView):
    model = Colaboradores


