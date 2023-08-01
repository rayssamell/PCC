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
            trabalhos_academicos = form.save(commit=False)
            trabalhos_academicos.usuario = request.user.usuario
            trabalhos_academicos.save()
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
    trabalhos_academicos = Trabalhos_academicos.objects.get(pk=id)

    if request.method == "POST":
        form = TrabalhosForm(request.POST, instance=trabalhos_academicos)
        if form.is_valid():
            form.save()
            return render(request, "trabalhos/listar.html")
    else:
        form = TrabalhosForm(instance=trabalhos_academicos)

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
    trabalhos_academicos = request.user.trabalhos_academicos.all()
    return render(request, 'trabalhos/listar.html', {'trabalhos_academicos': trabalhos_academicos})
