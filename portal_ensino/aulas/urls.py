from django.urls import path
from .views import aula, aula_anterior, proxima_aula, exercicio, reprovado, comentarios_delete
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('aula/', aula, name='aula'),
    path('proxima_aula/', proxima_aula, name='proxima_aula'),
    path('aula_anterior/', aula_anterior, name='aula_anterior'),
    # TESTE EXERCÍCIO
    path('exercicio/', exercicio, name='exercicio'),
    path('reprovado/', reprovado, name='reprovado'),
    path('deletar-comentario/<int:id>', comentarios_delete, name="deletar_comentario"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)