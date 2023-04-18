from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from hitcount.models import HitCount
from django.contrib.contenttypes.fields import GenericRelation
from django.shortcuts import reverse


User = get_user_model()


class Autor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user

    @property
    def num_forums(self):
        return Forum.objects.filter(user=self).count()


class Tema(models.Model):
    titulo = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    descricao = models.TextField(default="descrição")
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "temas"

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super(Tema, self).save(*args, **kwargs)

    def get_url(self):
        return reverse("forums", kwargs={
            "slug": self.slug
        })

    @property
    def num_temas(self):
        return Tema.objects.filter(temas=self).count()

    @property
    def last_forum(self):
        return Tema.objects.filter(temas=self).latest("data")


class Comentario(models.Model):
    user = models.ForeignKey(Autor, on_delete=models.CASCADE)
    conteudo = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.conteudo[:100]


class Forum(models.Model):
    titulo = models.CharField(max_length=400)
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    user = models.ForeignKey(Autor, on_delete=models.CASCADE)
    conteudo = models.TextField()
    temas = models.ForeignKey(Tema, on_delete=models.DO_NOTHING)
    data = models.DateTimeField(auto_now_add=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
                                        related_query_name='hit_count_generic_relation')
    comentario = models.ManyToManyField(Comentario, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super(Forum, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo

    def get_url(self):
        return reverse("detail", kwargs={
            "slug": self.slug
        })

    @property
    def num_comentarios(self):
        return self.comentarios.count()
