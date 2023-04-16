from django.db import models
from django.contrib.auth.models import User

class Usuarios(models.Model):
    nome = models.CharField(max_length=150)
    email=models.EmailField()
    cpf = models.IntegerField()
    endereco = models.CharField(max_length=150)
    telefone = models.CharField(max_length=15)
    descricao = models.TextField()

class Atuacao_Profissional(models.Model):
    nome_empresa = models.CharField(max_length=150)
    dia_hrs_atendimento = models.DateTimeField()
    cpf_usuario = models.IntegerField()

class Formacao(models.Model):
    universidade = models.CharField(max_length=150)
    grau_academico = models.CharField(max_length=100)
    especializacao = models.CharField(max_length=100)

class Trabalhos_academicos(models.Model):
    titulo_trabalho = models.CharField(max_length=150)
    autores = models.CharField(max_length=200)
    revista = models.CharField(max_length=150)
    ano = models.DateField()
    cpf_usuario = models.IntegerField()