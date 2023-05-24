from django.db import models


class Especialidade(models.Model):
    especialidade_add = models.CharField(max_length=100, null=True, 
                                         blank=True)

    def __str__(self):
        return f'{self.especialidade_add}'


class Atuacao_Profissional(models.Model):
    nome_da_empresa = models.CharField(max_length=150)
    dias_atendimento = models.DateField(null=True, blank=True)
    horario_atendimento = models.TimeField(null=True, blank=True)
    especialidade = models.ForeignKey(Especialidade,
                                      on_delete=models.DO_NOTHING,
                                      blank=False, null=False)

    def __str__(self):
        return f'{self.especialidade}'
