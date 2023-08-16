from django.db import models
from django.urls import reverse


class empresa(models.Model):
    nome = models.CharField(max_length=100, help_text="Nome da empresa")

    def __str__(self):
        return self.nome

    def get_absolut_url(self):
        return reverse('home')
