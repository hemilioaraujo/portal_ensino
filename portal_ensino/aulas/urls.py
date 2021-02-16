from django.urls import path
from portal_ensino.aulas.views import aula, proxima_aula, aula_anterior

urlpatterns = [
    path('', aula, name='aula'),
    path('proxima_aula/', proxima_aula, name='proxima_aula'),
    path('aula_anterior/', aula_anterior, name='aula_anterior'),
]
