from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth import authenticate, login, logout

def cadastro(request):
    if request.user.is_authenticated:
        #return redirect('/divulgar')
        return HttpResponse('Cadastro Concluido')
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        nome = request.POST.get('firstname')
        sobrenome = request.POST.get('lastname')
        email = request.POST.get('email')
        senha = request.POST.get('pass')
        confirmar_senha = request.POST.get('confirmar_senha')

        if len(nome.strip()) == 0 or len(sobrenome.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0 or len(confirmar_senha.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos.')
            return render(request, 'cadastro.html')
        
        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'Digite duas senhas iguais.')
            return render(request, 'cadastro.html')

        try:
            user = User.objects.create_user(
                username=nome,
                email=email,
                password=senha,
            )
            messages.add_message(request, constants.SUCCESS, 'Usuário criado com sucesso.')
            return render(request, 'cadastro.html')
        # Exceção
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema.')
            return render(request, 'cadastro.html')

def logar(request):
    if request.user.is_authenticated:
        #return redirect('/divulgar')
        return HttpResponse('Cadastro Concluido')
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        email = request.POST.get('email')
        senha = request.POST.get('pass')
        user = authenticate(username=email,
                            password=senha)

        if user is not None:
            login(request, user)
            #return redirect('/divulgar/novo_pet')
            return HttpResponse('Login Concluido')
        else:
            messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos')
            return render(request, 'login.html')


def sair(request):
    logout(request)
    return redirect('/auth/login')
    