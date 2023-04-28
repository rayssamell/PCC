from django.urls import path
from . import views


urlpatterns = [
    path('listar/', views.listarAtuacaoProfissinal, name='listar'),
    path('excluir/<int:id>/', views.excluirAtuacaoProfissional,
         name='excluir'),
    path('criar/', views.criarAtuacaoProfissional, name='criar'),
    path('editar/<int:id>/', views.atualizarAtuacaoProfissional,
         name='editar'),
]
