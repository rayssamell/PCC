from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404
from accounts.forms import UserRegisterForm, PerfilForm
from django.contrib.auth.decorators import login_required
from .models import Usuario
from .permissions import set_permission


def cadastrar(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            set_permission(user.usuario) 
            return redirect('/accounts/login')
    else:
        form = UserRegisterForm()

    context = {
        'form': form
    }
    return render(request, 'registration/register.html', context)


@login_required
def perfil_profissional(request, id):
    profissional = get_object_or_404(Usuario, id=id, tipoUsuario='P')
    context = {
        'user': profissional
    }
    return render(request, 'perfil/perfil_profissional.html', context)


@login_required
def perfil(request):
    usuario = request.user.usuario
    formacoes = usuario.formacao.all()
    atuacoes = usuario.atuacao_profissional.all()

    context = {
        'user': usuario,
        'formacoes': formacoes,
        'atuacoes': atuacoes
    }
    return render(request, 'perfil/perfil_profissional.html', context)


@login_required
def editarPerfil(request):
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=request.user.usuario)
        if form.is_valid():
            form.save()
            return redirect('perfil')
            
    else:
        form = PerfilForm(instance=request.user.usuario)

    context = {
        'user': request.user.usuario,
        'form': form,
    }
    
    return render(request, 'perfil/editarPerfil.html', context)


@login_required
def excluirPerfil(request, usuario_id):
    Usuario.objects.get(pk=usuario_id).delete()
    return render(request, 'perfil/perfil_profissional.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('/accounts/login')