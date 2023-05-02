from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .models import Sala, Mensagem
from django.contrib.auth.decorators import login_required
from .utils import update_views
from django.contrib.auth.models import User
from .forms import SalaForm, MensagemForm


@login_required
def listarSala(request):
    salas = Sala.objects.all()
    num_mensagens = Mensagem.objects.all().count()
    num_users = User.objects.all().count()

    try:
        last_mensagens = Mensagem.objects.latest("data")
    except:
        last_mensagens = []

    context = {
        "salas": salas,
        "num_mensagens": num_mensagens,
        "last_mensagens": last_mensagens,
        "num_users": num_users
    }
    return render(request, 'forum/salas.html', context)


@login_required
def criarSala(request):
    if request.method == "POST":
        form = SalaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("forum/listar_sala")
    else:
        form = SalaForm()

        context = {
            'form': form
    }

        return render(request, "forum/criar_sala.html", context)


@login_required
def atualizarSala(request, slug):
    salas = Sala.objects.get(slug=slug)

    if request.method == "POST":
        form = SalaForm(request.POST, instance=salas)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("forum/listar_sala")
    else:
        form = SalaForm(instance=salas)

    context = {
        'form': form,
        'slug': slug
    }

    return render(request, "forum/atualizar_sala.html", context)


@login_required
def excluirSala(request, slug):
    Sala.objects.get(slug=slug).delete()
    return HttpResponseRedirect("forum/listar_sala")


@login_required
def comentar(request):
    if request.method == "POST":
        form = MensagemForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/forum/mensagens")
    else:
        form = MensagemForm()

    context = {
        'form': form
    }

    return render(request, "forum/mensagens.html", context)


@login_required
def detail(request, slug):
    sala = get_object_or_404(Sala, slug=slug)
    if request.user.is_authenticated:
        autor = User.objects.get(user=request.user)

    if "mensagens-form" in request.POST:
        mensagem, = request.POST.get("mensagem")
        nova_mensagem, created = Mensagem.objects.get_or_create(
                                  user=autor, content=mensagem)
        sala.mensagem.add(nova_mensagem.id)

    context = {
        "sala": sala,
    }
    update_views(request, sala)

    return render(request, "detail.html", context)


@login_required
def listarMensagens(request, slug):
    sala = get_object_or_404(Sala, slug=slug)
    if request.user.is_authenticated:
        autor = User.objects.get(user=request.user)

    if "mensagens-form" in request.POST:
        mensagem, = request.POST.get("mensagem")
        nova_mensagem, created = Mensagem.objects.get_or_create(
                                  user=autor, content=mensagem)
        sala.mensagem.add(nova_mensagem.id)

    context = {
        "sala": sala,
    }
    update_views(request, sala)

    return render(request, "forum/mensagens.html", context)

