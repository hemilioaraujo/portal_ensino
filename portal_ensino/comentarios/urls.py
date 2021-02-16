from django.urls import path
from portal_ensino.comentarios.views import delete_comentario

urlpatterns = [
    path('deletar_comentario/<int:id>', delete_comentario, name="deletar_comentario"),
]
