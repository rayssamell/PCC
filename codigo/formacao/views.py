from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import FormacaoForm
from .models import Formacao


@login_required
def listar(request):
    formacao = Formacao.objects.all()
    return render(request, 'formacao/listar.html', {'formacao': formacao})


@login_required
def detail(request, id):
    formacao = Formacao.objects.get(pk=id)
    context = {
        "formacao": formacao
    }
    return render(request, 'formacao/detail.html', context)


@login_required
def criar(request):

    if request.method == "POST":
        form = FormacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/formacao/listar")
    else:
        form = FormacaoForm()

    context = {
        'form': form
    }

    return render(request, "formacao/criar.html", context)


@login_required
def excluir(request, id):
    Formacao.objects.get(pk=id).delete()

    return HttpResponseRedirect("/formacao/listar")    


@login_required
def editar(request, id):
    formacao = Formacao.objects.get(pk=id)

    if request.method == "POST":
        form = FormacaoForm(request.POST, instance=formacao)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/formacao/listar")
    else:
        form = FormacaoForm(instance=formacao)

    context = {
        'form': form,
        'id': id
    }

    return render(request, "formacao/editar.html", context)
