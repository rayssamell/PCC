from django.db import models


class Atuacao_Profissional(models.Model):
    especialidade_CHOICES = [
        ('analista do comportamento', 'Analista do comportamento'),
        ('fonoaudiologo', 'Fonoaudiólogo'),
        ('psicopedagogo', 'Psicopedagogo'),
        ('terapeuta ocupacional', 'Terapeuta ocupacional'),
        ('fisioterapeutas', 'Fisioterapeutas'),
        ('musicoterapia', 'Musicoterapia'),
        ('acompanhante terapêutico', 'Acompanhante Terapêutico'),
        ('psicologo', 'Psicologo'),
        ('neurologista', 'Neurologista'),
        ('psiquiatra', 'Psiquiatra'),
        ('pediatra', 'Pediatra'),
        ('psicomotricista', 'Psicomotricista')
    ]
    nome_da_empresa = models.CharField(max_length=150)
    dias_atendimento = models.DateField(null=True, blank=True)
    horario_atendimento = models.TimeField(null=True, blank=True)
    especialidade = models.CharField(
        max_length=25,
        choices=especialidade_CHOICES,
        default='psicologo'
    )

    def __str__(self):
        return f'{self.especialidade}'
