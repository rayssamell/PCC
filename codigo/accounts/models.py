from django.db import models
from django.contrib.auth.models import User
from atuacao_profissional.models import Atuacao_Profissional
from formacao.models import Formacao
from forum.models import Forum


class Usuario(User):
    cpf = models.CharField(max_length=14, blank=True, null=True)
    endereco = models.CharField(max_length=150, null=True)
    telefone = models.CharField(max_length=15)
    descricao = models.TextField(default='', blank=True)
    especialidade = models.ManyToManyField(Atuacao_Profissional)
    formacao = models.ManyToManyField(Formacao)
    forum = models.ManyToManyField(Forum)

    def __str__(self):
        return f'{self.user}'


