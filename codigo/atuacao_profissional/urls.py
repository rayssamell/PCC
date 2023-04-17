from django.urls import path
from . import views


urlpatterns = [
    path('', views.principal, name='principal'),
    path('home', views.home, name='home'),
    path('atuacao/', views.atuacao, name='atuacao')
]