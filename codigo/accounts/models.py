from django.db import models
from django.contrib.auth.models import User
from atuacao_profissional.models import Atuacao_Profissional
from formacao.models import Formacao
from forum.models import Sala
from multiselectfield import MultiSelectField
from trabalhos_academicos.models import Trabalhos_academicos


class Usuario(User):
    tipo_CHOICES = [
        ('P', 'Profissional'),
        ('F', 'Familiar'),
    ]
    cpf = models.CharField(max_length=14, blank=False, null=False, default='')
    endereco = models.CharField(max_length=150, null=True)
    telefone = models.CharField(max_length=15)
    descricao = models.TextField(default='', blank=True)
    atuacao_profissional = models.ManyToManyField(Atuacao_Profissional)
    formacao = models.ManyToManyField(Formacao)
    sala = models.ManyToManyField(Sala)
    trabalhos_academicos = models.ForeignKey(Trabalhos_academicos,
                                             on_delete=models.DO_NOTHING,
                                             null=True, blank=True)
    img = models.ImageField(upload_to='media/perfil', blank=True)
    tipoUsuario =  MultiSelectField(
        max_length=12,
        choices=tipo_CHOICES,
        max_choices=1
    )

    def __str__(self):
        return f'{self.nome}'

