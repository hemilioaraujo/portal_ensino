from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from portal_ensino.api import views


urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('hello-protected/', views.HelloViewProtected.as_view(), name='hello_protected'),

    # USER
    path('user/get/', views.UserAPI.get, name='get_user_api'),
    path('user/post/', views.UserAPI.post, name='post_user_api'),
    path('user/put/', views.UserAPI.put, name='put_user_api'),
    path('user/delete/', views.UserAPI.delete, name='delete_user_api'),
    path('user/new/', views.CreateUserAPI.as_view(), name='new_user_api'),

    # AULA
    path('aula/get/', views.AulaAPI.get, name='get_aula_api'),
    path('aula/proxima/', views.AulaAPI.proxima, name='proxima_aula_api'),
    path('aula/anterior/', views.AulaAPI.anterior, name='anterior_aula_api'),

    # COMENTÁRIOS
    path('comentario/get/all/', views.ComentarioAPI.get, name='lista_comentario'),
    path('comentario/post/', views.ComentarioAPI.post, name='novo_comentario'),
    path('comentario/delete/<int:id>/', views.ComentarioAPI.delete, name='excluir_comentario'),

    # EXERCÍCIOS
    path('exercicio/get/all/', views.QuestaoAPI.get, name='lista_exercicio'),
    path('exercicio/post/', views.QuestaoAPI.post, name='envia_exercicio'),


    # GET TOKEN
    path('token-request/', obtain_auth_token, name='token-request'),
]
