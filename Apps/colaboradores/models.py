from django.db import models
from django.contrib.auth.models import User
from Apps.departamentos.models import Departamento
from Apps.empresa.models import empresa

class Colaboradores(models.Model):
      nome = models.CharField(max_length=100)
      user = models.OneToOneField(User, on_delete=models.CASCADE)
      departamento = models.ManyToManyField(Departamento)
      empresa = models.ForeignKey(empresa, on_delete=models.PROTECT)


      def __str__(self):
          return self.nome