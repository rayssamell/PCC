from django.urls import path
from . import views


urlpatterns = [
    # http://127.0.0.1:8000/accounts/cadastrar/
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('perfil/', views.perfil, name='perfil'),
    path('preencher_perfil', views.preencherPerfil, name='preencher_perfil'),
    path('perfil/atualizar/', views.atualizar_perfil, name='atualizar_perfil'),

]
