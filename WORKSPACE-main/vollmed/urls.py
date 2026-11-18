"""
URL configuration for vollmed project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
import sistema.urls # forma diferente de importar

# VIEWS -> retornam algo, são funções, request -> response
# view responsável pela tela inicial do médico
def medico_view(request):
    print('Página médico funcionou')
    return HttpResponse ('Página inicial do Médico')

def home(request):
    print ('Página home funcionou')
    return HttpResponse ('Página Home')

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', include(sistema.urls)),
    path ('', include ('sistema/urls.py')) #precisa chamar as urls do app portal
    # path ('') #precisa chamar as urls do app portal
,]

# www.vollmed.online/
# www.vollmed.online/Login
# www.vollmed.online/

# MEDICO
# www.vollmed.online/medico/id/ -> Perfil do médico
# www.vollmed.online/medico/id/alterar -> Alterar cadastro do médico

# www.vollmed.online/medico/id/consultas

# PACIENTE
# www.vollmed.online/paciente/id/ -> Perfil do paciente
# www.vollmed.online/paciente/id/alterar -> Alterar cadastro do paciente

# www.vollmed.online/paciente/id/consultas/cadastrar/
# www.vollmed.online/paciente/id/consultas/id/ -> ver, alterar, deletar.

# SECRETARIO/SUPERUSER
# www.vollmed.online/secretario/id/ -> Perfil do secretário
# www.vollmed.online/secreari/id/alterar -> Alterar cadastro do secretário

# www.vollmed.online/secretario/id/consultas/cadastrar/
# www.vollmed.online/secretario/id/consultas/id/ -> ver, alterar, deletar.

# CONSULTA