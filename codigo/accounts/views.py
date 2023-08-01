from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404
from accounts.forms import UserRegisterForm, PerfilForm
from .utils import send_email_to_profissional
from django.contrib.auth.decorators import login_required
from .models import Usuario
from .permissions import set_permission
from django.contrib import messages


def cadastrar(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.tipoUsuario = request.POST.get('tipoUsuario')
            usuario.save()
            set_permission(usuario)
            return redirect('/accounts/login')
    else:
        form = UserRegisterForm()

    context = {
        'form': form
    }
    return render(request, 'registration/register.html', context)


@login_required
def perfil(request):
    if request.user.usuario.tipoUsuario == 'F':
        # Lógica para renderizar o perfil do familiar
        return render(request, 'perfil/familiar.html')
    elif request.user.usuario.tipoUsuario == 'P':
        return render(request, 'perfil/profissional.html')
    else:
        return render(request, 'registration/login.html')


@login_required
def perfil_profissional(request, profissional_id):
    profissional = get_object_or_404(Usuario, id=profissional_id)
    email_profissional = profissional.email  # Obtém o email do profissional

    if request.method == 'POST':
        # Dados do formulário de contato
        name = request.POST['name']
        email = request.POST['email']
        msg_subject = request.POST['msg_subject']
        message = request.POST['message']

        # Envie o email para o profissional
        send_email_to_profissional(name, email, msg_subject, message, email_profissional)
        messages.success(request, 'Mensagem enviada com sucesso!')

    context = {
        'email_profissional': email_profissional,
        'profissional': profissional,
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