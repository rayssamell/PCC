from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import Usuario


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=100)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'username', 'email',
                  'password1', 'password2']


class PerfilForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'cpf', 'endereco', 'telefone', 
                  'img', 'descricao']

