from django import forms
from .models import Atuacao_Profissional


class ProfissaoForm(forms.ModelForm):
    class Meta:
        model = Atuacao_Profissional
        fields = "__all__"

