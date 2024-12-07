from django.contrib import admin
from .models import Cliente, Filme, Locacao

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone')
    search_fields = ('nome', 'email')


@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'genero', 'disponivel')
    search_fields = ('titulo', 'genero')
    list_filter = ('genero', 'disponivel')


@admin.register(Locacao)
class LocacaoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'filme', 'data_locacao', 'devolvido')
    list_filter = ('devolvido',)
    search_fields = ('cliente__nome', 'filme__titulo')
