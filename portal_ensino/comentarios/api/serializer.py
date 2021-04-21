from rest_framework import serializers
from portal_ensino.comentarios.models import Comentarios


class ComentarioSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    aula_referente = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Comentarios
        depth = 1
        fields = [
            'id',
            'aula_referente',
            'user',
            'comentario',
            'data_postagem'
        ]
