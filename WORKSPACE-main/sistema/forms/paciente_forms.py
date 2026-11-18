from django import forms
from sistema.models import *

class PacienteForm(forms.ModelForm):
    "No model paciente o CPF tem 11 char, mas aqui podemos aceitar até 14"
    cpf = forms.CharField (
        max_length=14,
        label="CPF",
    )
    class Meta:
        model = paciente
        fields = ['nome', 'sobrenome', 'email', 'telefone', 'cpf',]
        labels = {
            "nome": "Nome",
            "sobrenome": "Sobrenome",
            "email": "E-mail",
            "telefone": "Telefome",
            "cpf" : "CPF",
        }

