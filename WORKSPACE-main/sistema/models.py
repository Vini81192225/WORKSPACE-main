from django.db import models # orm do Django para declarar modelos no banco de dados.
from django.utils import timezone #útil para gerar data/hora atual no projeto

# Modelo que representa um paciente
# atributos -> nome, sobrenome, email, telefone, data de cadastro, mensagem, ativo(True/False).
class paciente(models.Model):
    nome = models.CharField(max_length=25) # nome do paciente
    sobrenome = models.CharField(max_length=50) # sobrenome do paciente
    email = models.EmailField() # email de contato do paciente
    telefone = models.CharField(max_length=20) # telefone de contato
    cpf = models.CharField(max_length=11) # cpf com 11 dígitos, sem traço e ponto.
    criacao_data = models.DateTimeField(default=timezone.now) # Data/hora do cadastro
    mensagem = models.TextField(blank=True) # campo opcional livre para mensagem 
    ativo = models.BooleanField (default=True) # campo de exclusão tópico

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

class medico(models.Model):
    nome = models.CharField(max_length=25) # nome do paciente
    sobrenome = models.CharField(max_length=50) # sobrenome do paciente
    email = models.EmailField() # email de contato do paciente
    telefone = models.CharField(max_length=20) # telefone de contato
    CRM = models.CharField(max_length=25) 
    especialidade = models.CharField(max_length=25)
    criacao_data = models.DateTimeField(default=timezone.now)
    mensagem = models.TextField(blank=True) # campo opcional livre para mensagem 
    ativo = models.BooleanField (default=True) # campo de exclusão tópico

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

class consulta(models.Model):
    paciente_id = models.ForeignKey(paciente, on_delete=models.CASCADE) # chave estrangeira
    medico_id = models.ForeignKey(medico, on_delete=models.CASCADE) # chave estrangeira
    data_consulta = models.DateTimeField(default=timezone.now) # data/hora da consulta
    ativa = models.BooleanField(default=True) # campo de exclusão lógica
    observacao = models.TextField(blank=True) # anotação opcional
    status = models.CharField(
        default='A',
        max_length=1,
        choices=[
            ('A', 'Agendada'),
            ('X', 'Cancelada'),
            ('C', 'Confirmada'),
            ('R', 'Realizada'),
        ]
    )