from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .forms import FormacaoForm
from .models import Formacao


@login_required
def listarFormacaoAcademica(request):
    formacao = Formacao.objects.all()
    return render(request, 'formacao/listar.html', {'formacao': formacao})


@login_required
@permission_required('accounts.profissional')
def criarFormacaoAcademica(request):

    if request.method == "POST":
        form = FormacaoForm(request.POST)
        if form.is_valid():
            formacao = form.save(commit=False)
            formacao.usuario = request.user
            formacao.save()
            return redirect("/formacao/listar")
    else:
        form = FormacaoForm()

    context = {
        'form': form
    }

    return render(request, "formacao/criar.html", context)


@login_required
@permission_required('accounts.profissional')
def excluirFormacaoAcademica(request, id):
    formacao = get_object_or_404(Formacao, id=id)
    formacao.delete()
    return redirect("/formacao/listar")

@login_required
@permission_required('accounts.profissional')
def atualizarFormacaoAcademica(request, id):
    formacao = Formacao.objects.get(pk=id)

    if request.method == "POST":
        form = FormacaoForm(request.POST, instance=formacao)
        if form.is_valid():
            form.save()
            return redirect("listar_formacao")
    else:
        form = FormacaoForm(instance=formacao)

    context = {
        'form': form,
        'id': id
    }

    return render(request, "formacao/editar.html", context)
