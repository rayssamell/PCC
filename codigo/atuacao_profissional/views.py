from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from .forms import ProfissaoForm
from .models import Atuacao_Profissional


def principal(request):
    return render(request, 'principal.html')


def home(request):
    return "Pagina Principal"


@login_required
def criarAtuacaoProfissional(request):

    if request.method == "POST":
        form = ProfissaoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/profissao/listar_profissao")
    else:
        form = ProfissaoForm()

    context = {
        'form': form
    }

    return render(request, "atuacao_profissional/criar.html", context)


@login_required
def listarAtuacaoProfissional(request):
    profissao = Atuacao_Profissional.objects.all()
    return render(request, 'atuacao_profissional/listar.html',
                  {'profissao': profissao})


@login_required
def excluirAtuacaoProfissional(request, id):
    Atuacao_Profissional.objects.get(pk=id).delete()
    return HttpResponseRedirect("/profissao/listar_profissao")    


@login_required
def atualizarAtuacaoProfissional(request, id):
    profissao = Atuacao_Profissional.objects.get(pk=id)

    if request.method == "POST":
        form = ProfissaoForm(request.POST, instance=profissao)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/profissao/listar")
    else:
        form = ProfissaoForm(instance=profissao)

    context = {
        'form': form,
        'id': id
    }

    return render(request, "atuacao_profissional/editar.html", context)
