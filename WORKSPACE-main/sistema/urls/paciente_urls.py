from django.urls import path
from sistema.urls import *


# vollmed.com/admin
# vollmed.com/paciente => index
# vollmed.com/paciente/novo => index

urlpatterns = [
    path('paciente/', index_paciente), # vollmed.com/paciente
    #path('paciente_novo/'), # vollmed.com/paciente/novo
    #path('paciente/perfil/<int:paciente_id>'), # vollmed.com/paciente/perfil/<int:paciente_id>
    #path('paciente/listagem'), # vollmed.com/paciente/listagem
]
# path variable