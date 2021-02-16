from django.urls import path
from portal_ensino.base.views import xpto
from portal_ensino.questoes.views import exercicio

urlpatterns = [
    # XPTO
    path('exercicio/', exercicio, name='exercicio'),
    path('reprovado/', xpto, name='reprovado'),
]
