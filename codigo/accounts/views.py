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
def atualizarPerfil(request):
    context = {}
    user = request.user
    form = PerfilForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            atualizar_perfil = form.save(commit=False)
            atualizar_perfil.user = user
            atualizar_perfil.save()
            return redirect("home")

    context.update({
        "form": form,
        "title": "Atualizar Perfil",
    })
    return render(request, "perfil/perfil.html", context)


def editarPerfil(request):
    perfil = Usuario.objects.get(pk=id)

    if request.method == "POST":
        form = PerfilForm(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/atualizar_perfil/")
    else:
        form = PerfilForm(instance=perfil)

    context = {
        'form': form,
        'id': id
    }

    return render(request, "perfil/perfil.html", context)



def excluirPerfil(request):
    ...


def criarPerfil(request):
    ...
