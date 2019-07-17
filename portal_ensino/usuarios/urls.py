from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import usuarios_list, usuarios_novo, my_logout, do_login


urlpatterns = [
    path('list/', usuarios_list, name='lista_usuarios'),
    path('novo/', usuarios_novo, name="novo_usuario"),
    path('logout/', my_logout, name="logout"),
    path('do_login/', do_login, name="login"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # possibilita visualizar imagens dos profiles