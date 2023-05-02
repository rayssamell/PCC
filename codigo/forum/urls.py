from django.urls import path
from .views import listarSala, criarSala, atualizarSala, excluirSala, comentar, \
                   detail, listarMensagens

urlpatterns = [
    path('listar_sala/', listarSala, name='listar_sala'),
    path('criar_sala/', criarSala, name='criar_sala'),
    path("excluir_sala/<slug>/", excluirSala, name="excluir_sala"),
    path("atualizar_sala/<slug>/", atualizarSala, name="atualizar_sala"),
    path("detail/<slug>/", detail, name="detail"),
    path("listar_mensagens", listarMensagens, name="listar_mensagens"),
    path('mensagens/', comentar, name='mensagens'),
]
