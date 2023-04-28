
from django.shortcuts import redirect, render, get_object_or_404
from .models import Autor, Tema, Forum, Comentario
from .forms import ForumForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def home(request):
    temas = Tema.objects.all()
    num_forums = Forum.objects.all().count()
    num_users = User.objects.all().count()
    num_temas = temas.count()
    try:
        last_forum = Forum.objects.lastest("data")
    except:
        last_forum = []

    context = {
        "forums": forums,
        "num_forums": num_forums,
        "num_users": num_users,
        "num_temas": num_temas,
        "last_forum": last_forum,
        "titulo": "Autismo em Foco"
    }
    return render(request, "forum/temas.html", context)


def detail(request, slug):
    forum = get_object_or_404(Forum, slug=slug)
    if request.user.is_authenticated:
        autor = Autor.objects.get(user=request.user)

    if "comentario-form" in request.POST:
        comentario = request.POST.get("comentario")
        new_comentario = Comentario.objects.get_or_create(
                                  user=autor, content=comentario)
        forum.comentarios.add(new_comentario.id)

    context = {
        "forum": forum,
        "titulo": "Autismo em Foco: "+forum.titulo,
    }

    return render(request, "forum/detail.html", context)


def forums(request, slug):
    tema = get_object_or_404(Tema, slug=slug)
    forums = Forum.objects.filter(approved=True, temas=tema)
    paginator = Paginator(forums, 5)
    page = request.GET.get("page")
    try:
        forums = paginator.page(page)
    except PageNotAnInteger:
        forums = paginator.page(1)
    except EmptyPage:
        forums = paginator.page(paginator.num_pages)

    context = {
        "forums": forums,
        "forum": tema,
        "title": "Autismo em Foco: forums"
    }

    return render(request, "forum/forums.html", context)


@login_required
def criar_forum(request):
    context = {}
    form = ForumForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            autor = Autor.objects.get(user=request.user)
            new_forum = form.save(commit=False)
            new_forum.user = autor
            new_forum.save()
            form.save_m2m()
            return redirect("home")
    context.update({
        "form": form,
        "titulo": "Autismo em Foco: Crie um novo Forum"
    })
    return render(request, "forum/criar_forum.html", context)


def latest_forums(request):
    forums = Forum.objects.all().filter(approved=True)[:10]
    context = {
        "forums": forums,
        "titulo": "Autismo em Foco: Ultimos 10 Posts"
    }

    return render(request, "forum/latest_forums.html", context)

