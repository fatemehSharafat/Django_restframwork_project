# from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import PosRegister, User
from .serializers import PosRegisterSerializer, UserSerializer


# PosRegister
class PosRegisterListView(APIView):

    def get(self, request, user_id):
        posregisters = PosRegister.objects.filter(user_id=user_id)
        serializer = PosRegisterSerializer(posregisters, many=True, context={'request': request})
        return Response(serializer.data)


class PosRegisterDetailView(APIView):

    def get(self, request, pk, user_id):
        try:
            posregister = PosRegister.objects.get(pk=pk,user_id=user_id)
        except PosRegister.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PosRegisterSerializer(posregister, context={'request': request})
        return Response(serializer.data)


# User
class UserListView(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True, context={'request': request})
        return Response(serializer.data)

class UserDetailView(APIView):

    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, context={'request': request})
        return Response(serializer.data)
