from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("perfil/", views.perfil, name="perfil"),
    path("registrar/", views.registrar, name="registrar"),
]