from django.db import models

# Create your models here.
from django.db import models

class Turma(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name='alunos')
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    idade = models.PositiveIntegerField(blank=True, null=True)
    data_inscricao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
