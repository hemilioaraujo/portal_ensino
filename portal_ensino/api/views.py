from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from portal_ensino.aulas.views import proxima_aula, aula_anterior
from portal_ensino.base.api.serializers import UserSerializer, CreateUserSerializer
from portal_ensino.aulas.api.serializers import AulaSerializer
from portal_ensino.aulas.models import Aulas
from portal_ensino.base.models import User
from portal_ensino.comentarios.api.serializer import ComentarioSerializer
from portal_ensino.comentarios.models import Comentarios


class HelloView(APIView):
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class HelloViewProtected(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Authenticated Hello, World!'}
        return Response(content)


class UserAPI:
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get_object(pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    @staticmethod
    @api_view(['GET'])
    def get(request):
        serialized = UserSerializer(User.objects.get(pk=request.user.id))
        return Response(serialized.data)

    @staticmethod
    @api_view(['POST'])
    def post(request):
        user = UserAPI.get_object(pk=request.user.id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    @api_view(['PUT'])
    def put(request):
        user = UserAPI.get_object(pk=request.user.id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    @api_view(['DELETE'])
    def delete(request):
        user = UserAPI.get_object(pk=request.user.id)
        if user.is_active:
            content = {'message': f'User {user.username} excluído com sucesso!'}
            user.delete()
            return Response(content, status=status.HTTP_200_OK)
        content = {'message': 'Usuário não existe!'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)


class CreateUserAPI(APIView):
    permission_classes = ()

    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AulaAPI:
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get_object(pk):
        try:
            return Aulas.objects.get(pk=pk)
        except Aulas.DoesNotExist:
            raise Http404

    @staticmethod
    @api_view(['GET'])
    def get(request):
        id = request.user.aula_atual.id
        serializer = AulaSerializer(Aulas.objects.get(pk=id))
        return Response(serializer.data)

    @staticmethod
    @api_view(['GET'])
    def proxima(request):
        proxima_aula(request=request)
        id = request.user.aula_atual.id
        serializer = AulaSerializer(Aulas.objects.get(pk=id))
        return Response(serializer.data)

    @staticmethod
    @api_view(['GET'])
    def anterior(request):
        aula_anterior(request=request)
        id = request.user.aula_atual.id
        serializer = AulaSerializer(Aulas.objects.get(pk=id))
        return Response(serializer.data)


class ComentarioAPI:
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get_object(pk):
        try:
            return Comentarios.objects.get(pk=pk)
        except Comentarios.DoesNotExist:
            raise Http404

    @staticmethod
    @api_view(['GET'])
    def get(request):
        user = UserAPI.get_object(request.user.id)
        comentarios = Comentarios.objects.filter(aula_referente=user.aula_atual)
        print(comentarios)
        serializer = ComentarioSerializer(comentarios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    @api_view(['POST'])
    def post(request):
        user = UserAPI.get_object(request.user.id)
        aula = user.aula_atual
        try:
            text = request.data['comentario']
        except:
            content = {'message': 'Campo comentario não recebido!'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        if text:
            comentario = Comentarios.objects.create(user=user, aula_referente=aula, comentario=text)
            content = {'message': 'Postado'}
            return Response(content, status=status.HTTP_201_CREATED)
        content = {'message': 'Comentário vazio!'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    @api_view(['DELETE'])
    def delete(request, id):
        user = UserAPI.get_object(request.user.id)
        aula = AulaAPI.get_object(user.aula_atual.id)
        comentario = ComentarioAPI.get_object(id)

        if user.id == comentario.user.id:
            content = {'message': f'Comentario: \'{comentario.comentario}\' removido!'}
            comentario.delete()
            return Response(content, status=status.HTTP_200_OK)
        content = {'message': 'Não encontrado ou não pertence a você!'}
        return Response(content, status=status.HTTP_403_FORBIDDEN)
