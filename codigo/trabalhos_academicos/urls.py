from django.urls import path
from . import views

urlpatterns = [
     path('listar/', views.listarTrabalhosAcademicos, name='listar_trabalhos'),
     path('excluir/<int:id>/', views.excluirTrabalhosAcademicos, name='excluir_trabalhos'),
     path('publicar/', views.publicarTrabalhosAcademicos, name='publicar_trabalhos'),
     path('atualizar/<int:id>/', views.atualizarTrabalhosAcademicos, name='atualizar_trabalhos'),

]
