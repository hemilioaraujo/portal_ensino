from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import home, sobre
from .usuarios import urls as urls_usuarios
from .aulas import urls as urls_aulas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('sobre/', sobre, name='sobre'),

    # redirecionapara app usuarios
    path('usuarios/', include(urls_usuarios)),

    # redirecionapara app aulas
    path('aulas/', include(urls_aulas)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # possibilita visualizar imagens dos profiles
