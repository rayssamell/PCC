from django.db import models


class Trabalhos_academicos(models.Model):
    titulo_trabalho = models.CharField('Título do Trabalho', max_length=150)
    autores = models.CharField('Autor(es)', max_length=100)
    revista = models.CharField(max_length=50)
    ano = models.DateField('Ano de Publicação', null=False, blank=False)
    anexo = models.FileField(upload_to='meusarquivos/', blank=False,
                             default='')

    def __str__(self):
        return f'{self.titulo_trabalho}'
