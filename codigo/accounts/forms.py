from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'tipoUsuario']


class PerfilForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'email', 'endereco', 
                  'telefone', 'descricao', 'img']