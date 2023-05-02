from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from hitcount.models import HitCount
from django.contrib.contenttypes.fields import GenericRelation


User = get_user_model()


class Mensagem(models.Model):
    conteudo = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    anexo = models.ImageField(upload_to='media/forum', blank=True)
    autor = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name_plural = "Mensagem"

    def __str__(self):
        return self.autor


class Sala(models.Model):
    titulo = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now=True)
    imagem = models.ImageField(upload_to='media', blank=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
                                        related_query_name='hit_count_generic_relation'
    )
    mensagens = models.ManyToManyField(Mensagem, blank=True)

    class Meta:
        verbose_name_plural = "Salas"

    def __str__(self):
        return self.titulo

    def get_url(self):
        return reverse("detail", kwargs={
            "slug": self.slug
        })

    @property
    def num_mensagens(self):
        return self.mensagens.count()

    @property
    def last_mensagens(self):
        return self.mensagens.latest("data")


