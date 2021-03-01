from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from portal_ensino.api import views

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('hello-protected/', views.HelloViewProtected.as_view(), name='hello_protected'),
    path('user/', views.UserAPI.as_view(), name='user_api'),



    # GET TOKEN
    path('token-request/', obtain_auth_token, name='token-request'),
]
