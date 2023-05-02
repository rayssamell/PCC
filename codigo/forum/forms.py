from django.forms import ModelForm
from .models import Sala, Mensagem


class SalaForm(ModelForm):
    class Meta:
        model = Sala
        fields = "__all__"


class MensagemForm(ModelForm):
    class Meta:
        model = Mensagem
        fields = "__all__"