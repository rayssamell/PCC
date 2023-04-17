from django import forms
from .models import Formacao


class FormacaoForm(forms.ModelForm):
    class Meta:
        model = Formacao
        fields = "__all__"
