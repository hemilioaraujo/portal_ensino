from rest_framework import serializers

from portal_ensino.questoes.models import Questoes


class QuestoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questoes
        depth = 1
        fields = '__all__'
