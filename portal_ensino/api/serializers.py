from datetime import datetime
from rest_framework import serializers

from portal_ensino.base.models import User


# class UserSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     first_name = serializers.CharField()
#     last_name = serializers.CharField()
#     email = serializers.EmailField()
#     bio = serializers.CharField()
#     instituicao = serializers.CharField()
#     data_nascimento = serializers.DateField()
#     foto = serializers.ImageField()
#     # aula_atual = serializers.
#
#     # def create(self, validated_data):
#     #     """
#     #     Create and return a new `Person` instance, given the validated data.
#     #     :param validated_data:
#     #     """
#     #     return User.objects.create(**validated_data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'bio',
            'instituicao',
            'data_nascimento',
            'foto',
            'aula_atual'
        ]