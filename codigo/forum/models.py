from django.db import models
from hitcount.models import HitCount
from django.contrib.contenttypes.fields import GenericRelation
from accounts.models import Usuario


class Mensagem(models.Model):
    conteudo = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    anexo = models.ImageField(upload_to='forum', blank=True, null=True)
    autor = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='mensagens')

    class Meta:
        verbose_name_plural = "Mensagem"

    def __str__(self):
        return f"{self.autor.username} - {self.conteudo} - {self.autor.img.url}"
    

class Sala(models.Model):
    titulo = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to='forum', blank=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
                                        related_query_name='hit_count_generic_relation'
    )
    mensagens = models.ManyToManyField(Mensagem, blank=True)

    class Meta:
        verbose_name_plural = "Salas"

    def __str__(self):
        return self.titulo
    
    @property
    def num_mensagens(self):
        return self.mensagens.count()

    def tem_anexo(self):
        return self.anexo is not None