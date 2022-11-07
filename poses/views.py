#from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import PosRegister , User
from .serializers import PosRegisterSerializer , UserSerializer

class PosRegisterListView(APIView):

    def get(self, request):
        posregisters = PosRegister.objects.all()
        serializer = PosRegisterSerializer(posregisters, many=True, context={'request': request})
        return Response(serializer.data)

class PosRegisterDetailView(APIView):

    def get(self, request, pk):
        try:
            posregister = PosRegister.objects.get(pk=pk)
        except PosRegister.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer= PosRegisterSerializer(posregister , context={'request': request})
        return Response(serializer.data)

class UserView(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True, context={'request': request})
        return Response(serializer.data)