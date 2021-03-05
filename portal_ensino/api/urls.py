from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from portal_ensino.api import views

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('hello-protected/', views.HelloViewProtected.as_view(), name='hello_protected'),
    # USER
    path('user/', views.UserAPI.as_view(), name='user_api'),
    path('user/new/', views.CreateUserAPI.as_view(), name='new_user_api'),

    path('aula/', views.AulaAPI.get_aula, name='aula_api'),

    # GET TOKEN
    path('token-request/', obtain_auth_token, name='token-request'),
]

