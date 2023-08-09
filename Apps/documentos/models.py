from django.db import models
from Apps.colaboradores.models import Colaboradores

class documentos(models.Model):
      descricao = models.CharField(max_length=100)
      dono = models.ForeignKey(Colaboradores, on_delete=models.PROTECT)

      def __str__(self):
          self.descricao