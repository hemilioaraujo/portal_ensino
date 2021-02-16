from django.urls import path, include
from portal_ensino.base.views import home, xpto, exibir_profile, sobre
from portal_ensino.base.views import usuarios_update, usuarios_delete, usuarios_novo
from portal_ensino.api import urls as urls_api
from portal_ensino.aulas import urls as urls_aulas
from portal_ensino.questoes import urls as urls_questoes
from portal_ensino.comentarios import urls as urls_comentarios

app_name = 'base'

urlpatterns = [
    path('', home, name='home'),
    path('profile/', exibir_profile, name='exibir_profile'),
    path('atualizar-usuario/', usuarios_update, name="atualizar_usuario"),
    path('deletar-usuario/<int:id>', usuarios_delete, name="deletar_usuario"),
    path('novo-usuario/', usuarios_novo, name='novo_usuario'),
    path('sobre/', sobre, name='sobre'),

    path('', xpto, name='password_reset'),

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
