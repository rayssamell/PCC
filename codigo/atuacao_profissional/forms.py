from django import forms
from .models import Atuacao_Profissional, Especialidade


class ProfissaoForm(forms.ModelForm):
    class Meta:
        model = Atuacao_Profissional
        fields = "__all__"


class BuscaEspecialidadeForm(forms.Form):
    especialidades = Especialidade.objects.all().values_list('especialidade_add', 'especialidade_add')
    especialidade = forms.ChoiceField(choices=especialidades, required=False, label='Selecione a Especialidade')