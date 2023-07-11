from django.urls import path

from . import views

urlpatterns = [
    path('listar/', views.listarFormacaoAcademica, name='listar_formacao'),
    path('excluir/<int:id>/', views.excluirFormacaoAcademica, name='excluir_formacao'),
    path('criar/', views.criarFormacaoAcademica, name='preencher_formacao'),
    path('editar/<int:id>/', views.atualizarFormacaoAcademica, name='editar_formacao'),
]
