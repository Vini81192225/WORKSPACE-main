from django import forms
from sistema.models import *

class PacienteForm(forms.ModelForm):

    # Declaramos o CPF de novo para aceitar até 14 caracteres ("123.456.789-01").
    # O clean_cpf() abaixo tira a pontuação e devolve só os 11 números.
    cpf = forms.CharField(
        label='CPF',
        max_length=14,
        help_text='Pode digitar com ou sem pontos e traço.',
        widget=forms.TextInput(attrs={'placeholder': '123.456.789-01', 'inputmode': 'numeric'}),
    )

    class Meta:
        model = paciente
        fields = ['nome', 'sobrenome', 'email', 'telefone', 'cpf', 'imagem']
        labels = {
            'nome': 'Nome', 'sobrenome': 'Sobrenome', 'email': 'E-mail',
            'telefone': 'Telefone', 'imagem': 'Foto (opcional)',
        }
        help_texts = {
            'telefone': 'Com DDD. Ex.: (21) 99999-9999',
        }
        error_messages = {                 # troca as mensagens padrão do Django
            'email': {'invalid': 'Digite um e-mail válido, como nome@exemplo.com.'},
            'nome': {'required': 'Informe o nome do paciente.'},
        }
        widgets = {
            'telefone': forms.TextInput(attrs={'placeholder': '(21) 99999-9999'}),
        }