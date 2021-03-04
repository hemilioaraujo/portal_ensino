from rest_framework import serializers
from portal_ensino.aulas.models import Aulas
from portal_ensino.base.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        depth = 1
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


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class AulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aulas
        fields = [
            'id',
            'titulo',
            'link',
            'material'
        ]
