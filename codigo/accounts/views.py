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
def perfil(request):
    usuario = Usuario.objects.all()
    context = {'usuario': usuario}
    return render(request, 'perfil/perfil.html', context)


@login_required
def criarPerfil(request):
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = form.save(commit=False)
            # Atribuir o usuário atual à instância do perfil
            usuario.user = request.user
            usuario.save()
            return redirect('/perfil/')  
    else:
        form = PerfilForm()

    return render(request, 'perfil/criarPerfil.html', {'form': form})


@login_required
def editarPerfil(request):
    perfil = request.user
    
    if request.method == "POST":
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("perfil/")
    else:
        form = PerfilForm(instance=perfil)
    
    context = {
        'form': form,
        'usuario_id': usuario_id
    }

    return render(request, 'perfil/editarPerfil.html', context)


def excluirPerfil(request, usuario_id):
    Usuario.objects.get(id=usuario_id).delete()
    return render(request, 'perfil/perfil.html')
