from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from accounts.forms import UserRegisterForm, PerfilForm
from django.contrib.auth.decorators import login_required
from .models import Usuario


def cadastrar(request):

    form = UserRegisterForm

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/accounts/login")

    context = {
        'form': form
    }

    return render(request, 'registration/register.html', context=context)


@login_required
def perfil(request):
    usuario = Usuario.objects.all()
    context = {'usuario': usuario}
    return render(request, 'perfil/perfil.html', context)


@login_required
def preencherPerfil(request):
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES)
        if form.is_valid():
            perfil = form.save(commit=False)
            perfil.user = request.user
            perfil.save()
            return redirect('perfil')
    else:
        form = PerfilForm()
    return render(request, 'perfil/preencher_perfil.html', {'form': form})


def atualizar_perfil(request):
    perfil = request.user.usuario
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = PerfilForm(instance=perfil)
    return render(request, 'perfil/atualizar_perfil.html', {'form': form})


    

def excluirPerfil(request):
    ...


def criarPerfil(request):
    ...
