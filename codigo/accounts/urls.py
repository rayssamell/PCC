from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/accounts/cadastrar/
    path('cadastrar/', views.RegisterUser, name='cadastrar'),
]