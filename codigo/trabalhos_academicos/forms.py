from django import forms
from .models import Trabalhos_academicos


class TrabalhosForm(forms.ModelForm):
    class Meta:
        model = Trabalhos_academicos
        fields = "__all__"
