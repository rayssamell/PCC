from django.urls import path
from .views import sala, editar_mensagem, \
                   deletar_mensagem, criar_sala, \
                   atualizar_sala, detalhes_sala, excluir_sala

urlpatterns = [
    path('', sala, name='listar_sala'),
    path('salas/<int:sala_id>/mensagem/<int:mensagem_id>/editar/', 
         editar_mensagem, name='editar_mensagem'),
    path('salas/<int:sala_id>/mensagem/<int:mensagem_id>/excluir/', 
         deletar_mensagem, name='deletar_mensagem'),
    path('criar_sala/', criar_sala, name='criar_sala'),
    path('atualizar/<int:sala_id>/', atualizar_sala, name='atualizar_sala'),
    path('<int:sala_id>/', detalhes_sala, name='detalhes_sala'),
    path('salas/<int:sala_id>/excluir/', excluir_sala, 
         name='excluir_sala'),
    ]
