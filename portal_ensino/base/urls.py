from django.urls import path, include
from portal_ensino.base.views import home, xpto, exibir_profile, usuarios_update
from portal_ensino.api import urls as urls_api
from portal_ensino.aulas import urls as urls_aulas
from portal_ensino.questoes import urls as urls_questoes
from portal_ensino.comentarios import urls as urls_comentarios

app_name = 'base'

urlpatterns = [
    path('', home, name='home'),
    path('profile/', exibir_profile, name='exibir_profile'),
    path('atualizar-usuario/', usuarios_update, name="atualizar_usuario"),

    path('deletar-usuario/<int:id>', xpto, name="deletar_usuario"),
    path('', xpto, name='novo_usuario'),
    path('', xpto, name='password_reset'),
    path('', xpto, name='sobre'),

    # LOGIN
    path('contas/', include('django.contrib.auth.urls')),

    # API
    path('api/', include(urls_api)),

    # AULAS
    path('aulas/', include(urls_aulas)),

    # EXERCICIOS
    path('exercicios/', include(urls_questoes)),

    # COMENTARIOS
    path('comentarios/', include(urls_comentarios)),
]
