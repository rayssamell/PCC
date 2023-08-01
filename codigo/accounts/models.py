from django.db import models
from django.contrib.auth.models import User
from atuacao_profissional.models import Atuacao_Profissional
from formacao.models import Formacao
from trabalhos_academicos.models import Trabalhos_academicos


class Usuario(User):
    tipo_CHOICES = [
        ('P', 'Profissional'),
        ('F', 'Familiar'),
    ]
    cpf = models.CharField(max_length=14, blank=False, null=False, default='')
    endereco = models.CharField(max_length=150, blank=True, null=True)
    telefone = models.CharField(max_length=15)
    descricao = models.TextField(default='', blank=True)
    atuacao_profissional = models.ManyToManyField(Atuacao_Profissional)
    formacao = models.ManyToManyField(Formacao)
    img = models.ImageField(upload_to='media/perfil', blank=True, default='')
    tipoUsuario = models.CharField(
        max_length=1,
        choices=tipo_CHOICES,
    )

    def __str__(self):
        return f'{self.username}'
