from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .models import Sala, Mensagem, User
from .forms import MensagemForm, SalaForm


@login_required
def listarSala(request):
    salas = Sala.objects.all()
    num_mensagens = Mensagem.objects.count()
    num_users = User.objects.count()

    context = {
        "salas": salas,
        "num_mensagens": num_mensagens,
        "num_users": num_users
    }
    return render(request, 'forum/home.html', context)


@login_required
def atualizarMensagens(request, mensagem_id, sala_id):
    sala = get_object_or_404(Sala, id=sala_id)
    mensagem = get_object_or_404(Mensagem, id=mensagem_id, autor=request.user)
    
    if request.method == 'POST':
        form = MensagemForm(request.POST, request.FILES, instance=mensagem)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mensagem editada com sucesso.')
            return redirect('detalhes_sala', sala_id=sala_id)
    else:
        form = MensagemForm(instance=mensagem)
    
    return render(request, 'editar_mensagem.html', {'form': form,
                                                    'sala': sala})


@login_required
def excluirMensagens(request, mensagem_id, sala_id):
    sala = get_object_or_404(Sala, id=sala_id)
    mensagem = get_object_or_404(Mensagem, id=mensagem_id, autor=request.user)
  
    if request.method == 'POST':
        mensagem.delete()
        messages.success(request, 'Mensagem excluída com sucesso.')
        return redirect('detalhes_sala', sala_id=sala_id)
  
    return render(request, 'forum/deletar_mensagem.html',
                  {'mensagem': mensagem, 'sala': sala})


@login_required
@permission_required("Administrador")
def criarSala(request):
    if request.method == 'POST':
        form = SalaForm(request.POST, request.FILES)
        if form.is_valid():
            sala = form.save()
            return redirect('detalhes_sala', sala_id=sala.id)
    else:
        form = SalaForm()
    
    return render(request, 'forum/criar_sala.html', {'form': form})


@login_required
def atualizarSala(request, sala_id):
    sala = Sala.objects.get(pk=sala_id)
    
    if request.method == "POST":
        form = SalaForm(request.POST, instance=sala)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = SalaForm(instance=sala)
    
    context = {
        'form': form,
        'sala_id': sala_id
    }
    
    return render(request, "forum/atualizar_sala.html", context)


@login_required
def detalhes_sala(request, sala_id):
    sala = get_object_or_404(Sala, id=sala_id)
    mensagens = sala.mensagens.all()
    
    if request.method == 'POST':
        form = MensagemForm(request.POST, request.FILES)
        if form.is_valid():
            mensagem = form.save(commit=False)
            mensagem.autor = request.user
            mensagem.save()
            sala.mensagens.add(mensagem)
            return redirect('detalhes_sala', sala_id=sala_id)
    else:
        form = MensagemForm()
    
    return render(request, 'forum/detalhes_sala.html', {'sala': sala,
                                                        'mensagens': mensagens,
                                                        'form': form})


@login_required
def excluirSala(request, sala_id):
    Sala.objects.get(id=sala_id).delete()
    return render(request, 'forum/home.html')