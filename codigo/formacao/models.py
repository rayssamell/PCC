from django.db import models


class Formacao(models.Model):
    universidade = models.CharField(max_length=150)
    grau_academico = models.CharField(max_length=100)
    especializacao = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.grau_academico}'
