from django.db import models
from django.contrib.auth.models import User


class Trabalhos_academicos(models.Model):
    titulo_trabalho = models.CharField('Título do Trabalho', max_length=150)
    autores = models.CharField('Autor(es)', max_length=100)
    revista = models.CharField(max_length=50, null=True)
    ano = models.IntegerField('Ano de Publicação', null=False, blank=False)
    anexo = models.FileField(upload_to='meusarquivos/', blank=False,
                             default='')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trabalhos_academicos')

    def __str__(self):
        return f'{self.titulo_trabalho}'
