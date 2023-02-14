from django.db import models

class Forum(models.Model):
    titulo = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)

class Tema(models.Model):
    titulo_forum = models.ForeignKey(Forum, on_delete=models.DO_NOTHING, null= False)
    conteudo = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
   # anexo = models.ImageField(upload_to='/media/')
