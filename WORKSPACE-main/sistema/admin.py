from django.contrib import admin
from sistema import models

# Register your models here.
@admin.register(models.paciente) # registando a classe paciente no portal do python
class pacienteadmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'telefone', 'ativo',)

@admin.register(models.medico)    
class medicoadmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'telefone', 'CRM', 'especialidade', 'ativo',)

@admin.register(models.consulta)
class consultaadmin(admin.ModelAdmin):
    list_display = ('id', 'paciente_id', 'medico_id', 'status',)    
