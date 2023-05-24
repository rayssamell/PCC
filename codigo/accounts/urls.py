from django.urls import path
from . import views


urlpatterns = [
    # http://127.0.0.1:8000/accounts/cadastrar/
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/preencher', views.criarPerfil, name='preencher_perfil'),
    path('perfil/atualizar/<int:usuario_id>/', views.editarPerfil,
         name='atualizar_perfil'),
    path('perfil/excluir/<int:usuario_id>/', views.excluirPerfil,
         name='excluir_perfil'),

]