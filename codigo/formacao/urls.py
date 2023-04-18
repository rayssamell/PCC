from django.urls import path

from . import views

urlpatterns = [
    path('listar/', views.listar, name='listar'),
    path('<int:id>/', views.detail, name='detail'),
    path('excluir/<int:id>/', views.excluir, name='excluir'),
    path('criar/', views.criar, name='criar'),
    path('editar/<int:id>/', views.editar, name='editar'),
]