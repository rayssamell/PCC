from django import forms
from .models import Mensagem, Sala


class MensagemForm(forms.ModelForm):
    class Meta:
        model = Mensagem
        fields = ['conteudo', 'anexo']


class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = ['titulo', 'imagem']

