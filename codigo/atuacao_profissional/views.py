from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .forms import ProfissaoForm


def principal(request):
    return '<h1> Template Principal </h1>'


def home(request):
    return "Pagina Principal"


@login_required
@permission_required
def atuacao(request):

    form = ProfissaoForm

    if form.is_valid():
        form.save()
        return redirect("Teste")

    context = {
        'form': form
    }

    return render(request, 'registration/login.html', context=context)
