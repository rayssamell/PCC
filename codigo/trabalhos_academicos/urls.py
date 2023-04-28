from django.urls import path
from . import views

urlpatterns = [
    path('listar_Trabalhos/', views.listarTrabalhosAcademicos,
         name='listar_Trabalhos'),
    path('excluir_Trabalhos/<int:id>/', views.excluirTrabalhosAcademicos,
         name='excluir_Trabalhos'),
    path('publicar_Trabalhos/', views.publicarTrabalhosAcademicos,
         name='publicar_Trabalhos'),
    path('atualizar_Trabalhos/<int:id>/', views.atualizarTrabalhosAcademicos,
         name='atualizar_Trabalhos'),

]
