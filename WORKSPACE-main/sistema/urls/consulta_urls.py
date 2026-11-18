from django.urls import path
from sistema.urls import consulta_view

urlpatterns = [
    path('consulta/', consulta_view),
]