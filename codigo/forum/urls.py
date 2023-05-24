from django.urls import path
from .views import listarSala, atualizarMensagens, \
                   excluirMensagens, criarSala, \
                   atualizarSala, detalhes_sala, excluirSala

urlpatterns = [
    path('', listarSala, name='listar_sala'),
    path('salas/<int:sala_id>/mensagem/<int:mensagem_id>/editar/', 
         atualizarMensagens, name='editar_mensagem'),
    path('salas/<int:sala_id>/mensagem/<int:mensagem_id>/excluir/', 
         excluirMensagens, name='deletar_mensagem'),
    path('criar_sala/', criarSala, name='criar_sala'),
    path('atualizar/<int:sala_id>/', atualizarSala, name='atualizar_sala'),
    path('<int:sala_id>/', detalhes_sala, name='detalhes_sala'),
    path('salas/<int:sala_id>/excluir/', excluirSala, 
         name='excluir_sala'),
    ]
