from django.conf import settings
from django.core.cache import cache
from django.db.models import Q
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin
from django.views.generic.list import ListView

from common.views import TitleMixin
from interactions.forms import ForumCommentForm
from .forms import SearchForm
from .models import Tema, Forum


class ForumListView(TitleMixin, ListView):
    model = Forum
    template_name = 'forum/listar.html'
    ordering = ('nome',)
    title = 'Autismo em Foco | Forum'
    paginate_by = settings.Forum_PAGINATE_BY

    def get_queryset(self):
        queryset = self.model.objects.cached_queryset()

        selected_category_slug = self.kwargs.get('tema_slug')
        search = self.request.GET.get('search')

        if search:
            queryset = queryset.filter(Q(name__icontains=search) |
                                       Q(description__icontains=search))
        elif selected_category_slug:
            queryset = queryset.filter(category__slug=selected_category_slug)

        return queryset.prefetch_related('autor').order_by(*self.ordering)

    def get_paginator_url(self):
        selected_tema_slug = self.kwargs.get('tema_slug')
        search = self.request.GET.get('search')

        if selected_tema_slug:
            return reverse('forum:tema', args=(selected_tema_slug,)) \
                            + '?page='
        elif search:
            return f'?search={search}&page='
        return reverse('forum:listar') + '?page='

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()

        temas = Tema.objects.cached_queryset().order_by('nome')
        popular_tema = self.model.objects.cached_popular_tema()

        context['temas'] = temas[:settings.Temas_PAGINATE_BY]
        context['popular_tema'] = popular_tema[:3]

        context['has_more_temas'] = temas.count() > settings.Temas_PAGINATE_BY # noqa E501
        context['selected_tema_slug'] = self.kwargs.get('tema_slug')
        context['paginator_url'] = self.get_paginator_url()
        context['user_autor'] = self.model.objects.user_autor_forum(self.request.user) # noqa E501
        context['form'] = SearchForm(initial={'search': self.request.GET.get('search')}) # noqa E501

        return context


class ForumDetailView(FormMixin, DetailView):
    model = Forum
    slug_url_kwarg = 'forum_slug'
    template_name = 'forum/forum_description.html'
    form_class = ForumCommentForm

    def _has_viewed(self, request):
        remote_addr = request.META.get('REMOTE_ADDR')
        forum_slug = self.kwargs.get(self.slug_url_kwarg)

        key = f'{remote_addr}_{forum_slug}'
        has_viewed = cache.get(key)

        if not has_viewed:
            cache.set(key, True, 60)
        return has_viewed

    def _increment_views(self):
        self.object.views += 1
        self.object.save()

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        if not self._has_viewed(request):
            self._increment_views()
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        comments = self.object.comments().order_by('-created_date')
        comments_count = comments.count()

        context['comments'] = comments[:settings.COMMENTS_PAGINATE_BY]
        context['comments_count'] = comments_count
        context['has_more_comments'] = comments_count > settings.COMMENTS_PAGINATE_BY  # noqa E501
        context['title'] = f'Autismo em Foco | {self.object.nome}'
        return context
