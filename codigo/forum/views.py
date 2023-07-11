from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Sala, Mensagem
from accounts.models import Usuario
from .forms import MensagemForm, SalaForm


@login_required
def listarSala(request):
    salas = Sala.objects.all()
    num_mensagens = Mensagem.objects.count()
    num_users = Usuario.objects.count()

    context = {
        "salas": salas,
        "num_mensagens": num_mensagens,
        "num_users": num_users
    }
    return render(request, 'forum/salas.html', context)


@login_required
def atualizarMensagens(request, sala_id, mensagem_id):
    sala = get_object_or_404(Sala, id=sala_id)
    mensagem = get_object_or_404(Mensagem, id=mensagem_id, autor=request.user.usuario)

    if request.method == 'POST':
        novo_conteudo = request.POST.get('novo_conteudo')
        mensagem.conteudo = novo_conteudo
        mensagem.save()
        return redirect('detalhes_sala', sala_id=sala_id)
    
    return render(request, 'forum/detalhes_sala.html', {'sala': sala, 'mensagens': mensagens})


@login_required
def excluirMensagens(request, sala_id, mensagem_id):
    sala = get_object_or_404(Sala, id=sala_id)
    mensagem = get_object_or_404(Mensagem, id=mensagem_id, autor=request.user.usuario)

    if request.method == 'POST':
        mensagem.delete()
        return redirect('detalhes_sala', sala_id=sala_id)
    
    return render(request, 'forum/detalhes_sala.html', {'sala': sala, 'mensagens': mensagens})


@login_required
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
def listarMensagens(request, sala_id):
    sala = get_object_or_404(Sala, id=sala_id)
    mensagens = sala.mensagens.all()
    
    if request.method == 'POST':
        form = MensagemForm(request.POST, request.FILES)
        if form.is_valid():
            mensagem = form.save(commit=False)
            mensagem.autor = request.user.usuario
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
    return render(request, 'forum/salas.html')