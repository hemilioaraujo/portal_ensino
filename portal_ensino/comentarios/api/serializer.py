from rest_framework import serializers
from portal_ensino.comentarios.models import Comentarios


class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentarios
        depth = 1
        fields = [
            'aula_referente',
            'user',
            'comentario',
            'data_postagem'
        ]
