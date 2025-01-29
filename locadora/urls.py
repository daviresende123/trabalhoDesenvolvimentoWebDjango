from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("perfil/", views.perfil, name="perfil"),
    path("registrar/", views.registrar, name="registrar"),
    path("filmes/", views.listar_filmes, name="listar_filmes"),  # Listar filmes disponíveis
    path("alugar/<int:filme_id>/", views.alugar_filme, name="alugar_filme"),  # Alugar um filme
]