from django.urls import path

from . import views

urlpatterns = [
    path('listar/', views.listarFormacaoAcademica, name='listar'),
    path('excluir/<int:id>/', views.excluirFormacaoAcademica, name='excluir'),
    path('criar/', views.criarFormacaoAcademica, name='criar'),
    path('editar/<int:id>/', views.atualizarFormacaoAcademica, name='editar'),
]
