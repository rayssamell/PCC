from django.urls import path
from . import views


urlpatterns = [
     # http://127.0.0.1:8000/accounts/cadastrar/
     path('cadastrar/', views.cadastrar, name='cadastrar'),
     path('perfil/<int:id>/', views.perfil_profissional, name='perfil_profissional'),
     path('perfil/', views.perfil, name='perfil'),
     path('perfil/atualizar/', views.editarPerfil, name='atualizar_perfil'),
     path('perfil/excluir/<int:usuario_id>/', views.excluirPerfil,
          name='excluir_perfil'),
     path('logout/', views.logout_view, name='logout'),

]