from django.urls import path
from portal_ensino.questoes.views import exercicio, reprovado

urlpatterns = [
    path('exercicio/', exercicio, name='exercicio'),
    path('reprovado/', reprovado, name='reprovado'),
]
