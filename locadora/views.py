from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import RegistrarForm  # Importe o formulário personalizado
from .models import Filme, Locacao
from django.utils import timezone

def home(request):
    return render(request, 'locadora/home.html')

@login_required
def perfil(request):
    return render(request, 'locadora/perfil.html', {'user': request.user})

def registrar(request):
    if request.method == 'POST':
        form = RegistrarForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Faz login automaticamente após o registro
            return redirect('login')  # Redireciona para a tela de login
    else:
        form = RegistrarForm()
    return render(request, 'registration/registrar.html', {'form': form})


def listar_filmes(request):
    filmes = Filme.objects.filter(disponivel=True)  # Filtra apenas filmes disponíveis
    return render(request, 'locadora/listar_filmes.html', {'filmes': filmes})


@login_required
def alugar_filme(request, filme_id):
    filme = get_object_or_404(Filme, id=filme_id, disponivel=True)  # Verifica se o filme está disponível
    if request.method == 'POST':
        # Cria uma nova locação
        Locacao.objects.create(
            cliente=request.user,
            filme=filme,
            data_locacao=timezone.now(),
            devolvido=False
        )
        filme.disponivel = False  # Marca o filme como indisponível
        filme.save()
        return redirect('perfil')  # Redireciona para o perfil após o aluguel
    return render(request, 'locadora/alugar_filme.html', {'filme': filme})