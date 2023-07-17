from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Trabalhos_academicos
from .forms import TrabalhosForm


@login_required
@permission_required('accounts.profissional')
def publicarTrabalhosAcademicos(request):
    if request.method == "POST":
        form = TrabalhosForm(request.POST, request.FILES)
        if form.is_valid():
            trabalhosAcademicos = form.save(commit=False)
            trabalhosAcademicos.usuario = request.user.usuario
            trabalhosAcademicos.save()
            return redirect('listar_trabalhos')
    else:
        form = TrabalhosForm()

    context = {
        'form': form,
    }

    return render(request, "trabalhos/publicar.html", context)


@login_required
@permission_required('accounts.profissional')
def atualizarTrabalhosAcademicos(request, id):
    trabalhosAcademicos = Trabalhos_academicos.objects.get(pk=id)

    if request.method == "POST":
        form = TrabalhosForm(request.POST, instance=trabalhosAcademicos)
        if form.is_valid():
            form.save()
            return render(request, "trabalhos/listar.html")
    else:
        form = TrabalhosForm(instance=trabalhosAcademicos)

    context = {
        'form': form,
        'id': id
    }

    return render(request, "trabalhos/atualizar.html", context)


@login_required
@permission_required('accounts.profissional')
def excluirTrabalhosAcademicos(request, id):
    Trabalhos_academicos.objects.get(pk=id).delete()
    return redirect('listar_trabalhos')


@login_required
def listarTrabalhosAcademicos(request):
    trabalhosAcademicos = Trabalhos_academicos.objects.all()
    return render(request, 'trabalhos/listar.html', {'trabalhosAcademicos': trabalhosAcademicos})
