from django.urls import path
from . import views


urlpatterns = [
    path('listar_profissao/', views.listarAtuacaoProfissional, name='listar_profissao'),
    path('excluir_profissao/<int:id>/', views.excluirAtuacaoProfissional,
         name='excluir_profissao'),
    path('criar_profissao/', views.criarAtuacaoProfissional, name='criar_profissao'),
    path('editar_profissao/<int:id>/', views.atualizarAtuacaoProfissional,
         name='editar'),
]
