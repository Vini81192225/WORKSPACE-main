from django import forms
from sistema.models import *

class ConsultaForm(forms.ModelForm):
    paciente_id = forms.CharField (
        max_length=14,
        label= "paciente ID"
    )
    class Meta:
        model = consulta
        fields = ['paciente_id', 'medico_id', 'data_consulta', 'ativa', 'observacao', 'status']
        labels = {
            "paciente_id" : "Paciente ID",
            "medico_id" : "Médico ID",
            "data_consulta" : "Data consulta",
            "ativa" : "Ativa",
            "observacao" : "Observação",
            "status" : "Status",
        }
