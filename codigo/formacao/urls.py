from django.urls import path
from . import views


urlpatterns = [
    path('', views.formacao, name='formacao'),
]
