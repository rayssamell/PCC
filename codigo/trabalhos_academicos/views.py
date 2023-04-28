from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Trabalhos_academicos
from .forms import TrabalhosForm


def publicarTrabalhosAcademicos(request):
    if request.method == "POST":
        form = TrabalhosForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/trabalhosAcademicos/listar_Trabalhos")
    else:
        form = TrabalhosForm()

    context = {
        'form': form
    }

    return render(request, "trabalhos/publicar.html", context)


def atualizarTrabalhosAcademicos(request, id):
    trabalhosAcademicos = Trabalhos_academicos.objects.get(pk=id)

    if request.method == "POST":
        form = TrabalhosForm(request.POST, instance=trabalhosAcademicos)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/trabalhosAcademicos/listar_Trabalhos")
    else:
        form = TrabalhosForm(instance=trabalhosAcademicos)

    context = {
        'form': form,
        'id': id
    }

    return render(request, "trabalhos/atualizar.html", context)


def excluirTrabalhosAcademicos(request, id):
    Trabalhos_academicos.objects.get(pk=id).delete()

    return HttpResponseRedirect("/trabalhosAcademicos/listar_Trabalhos")


def listarTrabalhosAcademicos(request):
    trabalhosAcademicos = Trabalhos_academicos.objects.all()
    return render(request, 'trabalhos/listar.html',
                  {'trabalhosAcademicos': trabalhosAcademicos})
