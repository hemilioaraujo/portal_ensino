from django.urls import path
from .views import aula
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('aula/', aula, name='aula'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)