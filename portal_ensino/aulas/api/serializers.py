from rest_framework import serializers

from portal_ensino.aulas.models import Aulas


class AulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aulas
        fields = [
            'id',
            'titulo',
            'link',
            'material'
        ]
