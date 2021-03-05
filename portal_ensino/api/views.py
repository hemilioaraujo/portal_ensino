from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from portal_ensino.base.api.serializers import UserSerializer, CreateUserSerializer
from portal_ensino.aulas.api.serializer import AulaSerializer
from portal_ensino.aulas.models import Aulas
from portal_ensino.base.models import User


class HelloView(APIView):
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class HelloViewProtected(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Authenticated Hello, World!'}
        return Response(content)


class UserAPI(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request):
        serialized = UserSerializer(User.objects.get(pk=request.user.id))
        return Response(serialized.data)

    def post(self, request):
        user = self.get_object(pk=request.user.id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        user = self.get_object(pk=request.user.id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        user = self.get_object(pk=request.user.id)
        if user.is_active:
            content = {'message': f'User {user.username} excluído com sucesso!'}
            user.delete()
            return Response(content, status=status.HTTP_200_OK)
        content = {'message': 'Usuário não existe!'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)


class CreateUserAPI(APIView):
    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AulaAPI:
    @staticmethod
    @api_view(['GET'])
    @permission_classes([IsAuthenticated])
    def get_aula(request):
        serializer = AulaSerializer(Aulas.objects.get(pk=1))
        return Response(serializer.data)
