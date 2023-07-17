from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .forms import BuscaEspecialidadeForm, ProfissaoForm
from .models import Atuacao_Profissional
from accounts.models import Usuario


def principal(request):
    return render(request, 'principal.html')


@login_required
@permission_required('accounts.profissional')
def criarAtuacaoProfissional(request):
    if request.method == 'POST':
        form = ProfissaoForm(request.POST)
        if form.is_valid():
            atuacao = form.save(commit=False)
            atuacao.usuario = request.user
            atuacao.save()
            return redirect('listar_atuacao')
    else:
        form = ProfissaoForm()
    return render(request, 'atuacao_profissional/criar.html', {'form': form})


@login_required
def listarAtuacaoProfissional(request):
    atuacao = Atuacao_Profissional.objects.all()
    return render(request, 'atuacao_profissional/listar.html',
                  {'atuacao': atuacao})


@login_required
@permission_required('accounts.profissional')
def excluirAtuacaoProfissional(request, id):
    atuacao = get_object_or_404(Atuacao_Profissional, id=id)
    atuacao.delete()
    return redirect("listar_atuacao")


@login_required
@permission_required('accounts.profissional')
def atualizarAtuacaoProfissional(request, id):
    atuacao = get_object_or_404(Atuacao_Profissional, id=id)

    if request.method == "POST":
        form = ProfissaoForm(request.POST, instance=atuacao)
        if form.is_valid():
            form.save()
            return redirect("listar_atuacao")
    else:
        form = ProfissaoForm(instance=atuacao)

    context = {
        'form': form,
        'atuacao': atuacao
    }

    return render(request, "atuacao_profissional/editar.html", context)


@login_required
def listarProfissionais(request):
    profissionais = Usuario.objects.filter(tipoUsuario='P')
    form = BuscaEspecialidadeForm(request.GET)

    if form.is_valid():
        especialidade = form.cleaned_data['especialidade']
        if especialidade:
            profissionais = profissionais.filter(atuacao_profissional__especialidade__especialidade_add=especialidade)

    context = {
        'profissionais': profissionais,
        'form': form,
    }

    return render(request, 'atuacao_profissional/profissionais.html', context)