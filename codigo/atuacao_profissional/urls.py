from django.urls import path
from . import views


urlpatterns = [
     path('autismoemfoco/', views.principal, name='autismo_em_foco'),
     path('listar_atuacao/', views.listarAtuacaoProfissional, 
          name='listar_atuacao'),
     path('preencher_atuacao/', views.criarAtuacaoProfissional, 
          name='preencher_atuacao'),
     path('atualizar_atuacao/<int:id>/', views.atualizarAtuacaoProfissional,
          name='atualizar_atuacao'),
     path('excluir_atuacao/<int:id>/', views.excluirAtuacaoProfissional,
          name='excluir_atuacao'),
     path('profissionais/', views.listarProfissionais, name='listar_profissionais'),
]
