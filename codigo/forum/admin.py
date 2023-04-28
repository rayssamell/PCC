from django.contrib import admin
from .models import Forum, Tema, Comentario


admin.site.register(Tema)
admin.site.register(Forum)
admin.site.register(Comentario)
