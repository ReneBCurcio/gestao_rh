from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import empresa
from django.http import HttpResponse



class empresaCreate(CreateView):
    model = empresa
    fields = ['nome']

#Retorna a empresa#
    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.colaboradores
        funcionario.empresa = obj
        funcionario.save()
        return HttpResponse('ok')
