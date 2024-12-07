from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    endereco = models.TextField()

    def __str__(self):
        return self.nome


class Filme(models.Model):
    titulo = models.CharField(max_length=200)
    genero = models.CharField(max_length=50)
    data_lancamento = models.DateField()
    descricao = models.TextField()
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo


class Locacao(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    data_locacao = models.DateField(auto_now_add=True)
    data_devolucao = models.DateField(null=True, blank=True)
    devolvido = models.BooleanField(default=False)

    def __str__(self):
        return f"Locação de {self.filme} para {self.cliente}"
