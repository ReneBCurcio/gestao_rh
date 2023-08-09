from django.db import models
from Apps.colaboradores.models import Colaboradores

class RegistroHoraExtra(models.Model):
      motivo = models.CharField(max_length=100)
      colaborador = models.ForeignKey(Colaboradores, on_delete=models.PROTECT)

      def __str__(self):
          return self.motivo
