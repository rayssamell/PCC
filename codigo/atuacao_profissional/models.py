from django.db import models
from multiselectfield import MultiSelectField


class Especialidade(models.Model):
    especialidade_add = models.CharField(max_length=100, null=True, 
                                         blank=True)

    def __str__(self):
        return f'{self.especialidade_add}'


class Atuacao_Profissional(models.Model):
    dias_CHOICES = [
        ('segunda', 'Segunda'),
        ('terça', 'Terça'),
        ('quarta', 'Quarta'),
        ('quinta', 'Quinta'),
        ('sexta', 'Sexta'),
        ('sabado', 'Sabado'),
    ]
    nome_da_empresa = models.CharField(max_length=150)
    dias_atendimento = MultiSelectField(
        max_length=50,
        choices=dias_CHOICES,
        max_choices=6, default='',
    )
    horario_atendimento = models.TimeField(null=True, blank=True)
    especialidade = models.ForeignKey(Especialidade,
                                      on_delete=models.DO_NOTHING,
                                      null=False)

    def __str__(self):
        return f'{self.especialidade}'


