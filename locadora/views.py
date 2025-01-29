from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import RegistrarForm  # Importe o formulário personalizado

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