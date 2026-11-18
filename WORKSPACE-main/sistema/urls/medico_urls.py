from django.urls import path
from sistema.urls import medico_view

urlpatterns = [
    path('medico/', medico_view),
]