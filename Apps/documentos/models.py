from django.db import models


class documentos(models.Model):
      descricao = models.CharField(max_length=100)

      def __str__(self):
          self.descricao